from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import Tratamiento, Consulta, Procedimiento
from .serializers import TratamientoSerializer, ConsultaSerializer, ProcedimientoSerializer

class TratamientoViewSet(viewsets.ModelViewSet):
    queryset = Tratamiento.objects.all()
    serializer_class = TratamientoSerializer

    @action(detail=False, methods=['get'])
    def buscar_por_nombre(self, request):
        nombre = request.query_params.get('nombre', None)
        if nombre:
            tratamientos = Tratamiento.objects.filter(nombre__icontains=nombre)
            serializer = self.get_serializer(tratamientos, many=True)
            return Response(serializer.data)
        return Response([])

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

    @action(detail=False, methods=['get'])
    def por_fecha(self, request):
        fecha = request.query_params.get('fecha', None)
        if fecha:
            consultas = Consulta.objects.filter(fecha=fecha)
            serializer = self.get_serializer(consultas, many=True)
            return Response(serializer.data)
        return Response([])

    @action(detail=False, methods=['get'])
    def por_paciente(self, request):
        paciente_id = request.query_params.get('paciente', None)
        if paciente_id:
            consultas = Consulta.objects.filter(paciente_id=paciente_id)
            serializer = self.get_serializer(consultas, many=True)
            return Response(serializer.data)
        return Response([])

class ProcedimientoViewSet(viewsets.ModelViewSet):
    queryset = Procedimiento.objects.all()
    serializer_class = ProcedimientoSerializer

    @action(detail=False, methods=['get'])
    def por_consulta(self, request):
        consulta_id = request.query_params.get('consulta', None)
        if consulta_id:
            procedimientos = Procedimiento.objects.filter(consulta_id=consulta_id)
            serializer = self.get_serializer(procedimientos, many=True)
            return Response(serializer.data)
        return Response([])
