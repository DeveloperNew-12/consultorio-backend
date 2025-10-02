from rest_framework import serializers
from .models import Cita

class CitaSerializer(serializers.ModelSerializer):
    # Campos adicionales para mostrar información relacionada
    paciente_nombre = serializers.CharField(source='paciente.nombres', read_only=True)
    odontologo_nombre = serializers.CharField(source='odontologo.nombre', read_only=True)
    
    class Meta:
        model = Cita
        fields = '__all__'
        extra_kwargs = {
            'idcita': {'read_only': True}
        }
