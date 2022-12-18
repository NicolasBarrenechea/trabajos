from django.shortcuts import render
from.models import Institucion
from rest_framework.decorators import api_view
from .serializers import InstitucionSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.



#------------------fbw--------------------------------


@api_view(['GET', 'POST'])
def institucion_list(request):
    if request.method == 'GET':
        inscri = Institucion.objects.all()
        serial = InstitucionSerializer(inscri, many=True)
        return Response(serial.data)
    
    if request.method == 'POST':
        serial = InstitucionSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def institucion_detail(request, id):
    try:
        inscri = Institucion.objects.get(id = id)
    except Institucion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serial = InstitucionSerializer(inscri)
        return Response(serial.data)

    if request.method == 'PUT':
        serial = InstitucionSerializer(inscri, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'DELETE':
        inscri.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)