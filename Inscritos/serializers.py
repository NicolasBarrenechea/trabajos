from rest_framework import serializers
from .models import Inscritos

class InscritosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscritos
        fields = '__all__'