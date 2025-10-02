from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Paciente, HistoriaClinica, Odontograma, PiezaDental, Adjunto
from .serializers import PacienteSerializer, HistoriaClinicaSerializer, OdontogramaSerializer, PiezaDentalSerializer, AdjuntoSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

    @action(detail=False, methods=['get'])
    def buscar_por_ci(self, request):
        ci = request.query_params.get('ci', None)
        if ci:
            pacientes = Paciente.objects.filter(ci__icontains=ci)
            serializer = self.get_serializer(pacientes, many=True)
            return Response(serializer.data)
        return Response([])

class HistoriaClinicaViewSet(viewsets.ModelViewSet):
    queryset = HistoriaClinica.objects.all()
    serializer_class = HistoriaClinicaSerializer

class OdontogramaViewSet(viewsets.ModelViewSet):
    queryset = Odontograma.objects.all()
    serializer_class = OdontogramaSerializer

class PiezaDentalViewSet(viewsets.ModelViewSet):
    queryset = PiezaDental.objects.all()
    serializer_class = PiezaDentalSerializer

class AdjuntoViewSet(viewsets.ModelViewSet):
    queryset = Adjunto.objects.all()
    serializer_class = AdjuntoSerializer
