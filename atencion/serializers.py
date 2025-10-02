from rest_framework import serializers
from .models import Tratamiento, Consulta, Procedimiento

class TratamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tratamiento
        fields = '__all__'

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'

class ProcedimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedimiento
        fields = '__all__'
