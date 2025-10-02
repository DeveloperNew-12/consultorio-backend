from rest_framework import serializers
from .models import Paciente, HistoriaClinica, Odontograma, PiezaDental, Adjunto

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'
        extra_kwargs = {
            'idpaciente': {'read_only': True}
        }

class HistoriaClinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoriaClinica
        fields = '__all__'

class OdontogramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Odontograma
        fields = '__all__'

class PiezaDentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PiezaDental
        fields = '__all__'

class AdjuntoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adjunto
        fields = '__all__'
