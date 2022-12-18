from django.shortcuts import render, get_object_or_404, redirect
from .models import Inscritos
from .forms import Inscritosform
from django.http import JsonResponse, Http404
from django.views import View
from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import InscritosSerializer


# Create your views here.

def index(request):
    return render(request, 'index.html')

def crud(request):
    inscritos = Inscritos.objects.all()
    listado={'inscritos':inscritos}
    return render(request, 'crud.html', listado)

def crear(request):
    formulario = {
        'form':Inscritosform}
    error = {'error': 'datos invalidos'}

    formerror = {'form':Inscritosform, 'error': 'datos invalidos'}
    ruta = 'crear.html'

    if request.method == 'GET':
        return render(request, ruta, formulario)
    else:

        Inscritosform(request.POST).save()
        return render(request, ruta, formulario)

    

def eliminar(request, id):
    inscrito = get_object_or_404(Inscritos, pk=id)
    if request.method == 'POST':
        inscrito.delete()
        return redirect('/crud')

    
def editar(request, id):
    if request.method == 'GET':
        inscritos = get_object_or_404(Inscritos, pk=id)
        form = Inscritosform(instance=inscritos)
        
        data = {'inscritos': inscritos, 'form': form}
        return render(request,'crear.html',data)
    else:
        inscritos = get_object_or_404(Inscritos, pk=id)
        form = Inscritosform(request.POST, instance=inscritos)
        form.save()
        return redirect('/crud')




#--------------------api rest---------------------------
class ApiRest (View):
    def get (self, request):
        inscritos = Inscritos.objects.all()
        data = {'inscritos' : list(inscritos.values())}
        return JsonResponse(data)



class ApiRestdetail (View):
    def get (self, request, pk):
        inscritos = Inscritos.objects.get(pk=pk)
        return JsonResponse(model_to_dict(inscritos))


#------------------------CBW----------------


class ListarInscritos(APIView):

    def get(self, request):
        estu = Inscritos.objects.all()
        serial = InscritosSerializer(estu, many=True)
        return Response(serial.data)

    def post(self, request):
        serial = InscritosSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DetalleInscritos(APIView):

    def get_object(self, pk):
        try:
            return Inscritos.objects.get(pk=pk)
        except Inscritos.DoesNotExist:
            return Http404
        
    def get(self, request, pk):
        inscri = self.get_object(pk)
        serial = InscritosSerializer(inscri)
        return Response(serial.data)

    def put(self, request, pk):
        inscri = self.get_object(pk)
        serial = InscritosSerializer(inscri, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        inscri = self.get_object(pk)
        inscri.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
