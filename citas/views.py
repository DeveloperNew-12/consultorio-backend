from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Cita
from .serializers import CitaSerializer

class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer

    @action(detail=False, methods=['get'])
    def por_fecha(self, request):
        fecha = request.query_params.get('fecha', None)
        if fecha:
            citas = Cita.objects.filter(fecha=fecha)
            serializer = self.get_serializer(citas, many=True)
            return Response(serializer.data)
        return Response([])

    @action(detail=False, methods=['get'])
    def por_estado(self, request):
        estado = request.query_params.get('estado', None)
        if estado:
            citas = Cita.objects.filter(estado=estado)
            serializer = self.get_serializer(citas, many=True)
            return Response(serializer.data)
        return Response([])

    @action(detail=False, methods=['get'])
    def hoy(self, request):
        hoy = timezone.now().date()
        citas = Cita.objects.filter(fecha=hoy)
        serializer = self.get_serializer(citas, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def proximas(self, request):
        """Obtener citas próximas (próximos 7 días)"""
        hoy = timezone.now().date()
        proxima_semana = hoy + timedelta(days=7)
        citas = Cita.objects.filter(
            fecha__range=[hoy, proxima_semana],
            estado__in=['Agendada', 'Confirmada']
        ).order_by('fecha', 'horarioini')
        serializer = self.get_serializer(citas, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def por_odontologo(self, request):
        """Obtener citas por odontólogo"""
        odontologo_id = request.query_params.get('odontologo', None)
        if odontologo_id:
            citas = Cita.objects.filter(odontologo_id=odontologo_id)
            serializer = self.get_serializer(citas, many=True)
            return Response(serializer.data)
        return Response([])

    @action(detail=False, methods=['get'])
    def por_paciente(self, request):
        """Obtener citas por paciente"""
        paciente_id = request.query_params.get('paciente', None)
        if paciente_id:
            citas = Cita.objects.filter(paciente_id=paciente_id)
            serializer = self.get_serializer(citas, many=True)
            return Response(serializer.data)
        return Response([])

    @action(detail=True, methods=['post'])
    def confirmar(self, request, pk=None):
        """Confirmar una cita"""
        cita = self.get_object()
        if cita.estado == 'Agendada':
            cita.estado = 'Confirmada'
            cita.save()
            serializer = self.get_serializer(cita)
            return Response({
                'mensaje': 'Cita confirmada exitosamente',
                'cita': serializer.data
            })
        return Response(
            {'error': 'Solo se pueden confirmar citas agendadas'}, 
            status=status.HTTP_400_BAD_REQUEST
        )

    @action(detail=True, methods=['post'])
    def cancelar(self, request, pk=None):
        """Cancelar una cita"""
        cita = self.get_object()
        motivo = request.data.get('motivo', 'Sin motivo especificado')
        
        if cita.estado in ['Agendada', 'Confirmada']:
            cita.estado = 'Cancelada'
            cita.motivo = f"{cita.motivo} - CANCELADA: {motivo}"
            cita.save()
            serializer = self.get_serializer(cita)
            return Response({
                'mensaje': 'Cita cancelada exitosamente',
                'cita': serializer.data
            })
        return Response(
            {'error': 'Solo se pueden cancelar citas agendadas o confirmadas'}, 
            status=status.HTTP_400_BAD_REQUEST
        )

    @action(detail=True, methods=['post'])
    def completar(self, request, pk=None):
        """Marcar una cita como completada"""
        cita = self.get_object()
        if cita.estado == 'Confirmada':
            cita.estado = 'Completada'
            cita.save()
            serializer = self.get_serializer(cita)
            return Response({
                'mensaje': 'Cita marcada como completada',
                'cita': serializer.data
            })
        return Response(
            {'error': 'Solo se pueden completar citas confirmadas'}, 
            status=status.HTTP_400_BAD_REQUEST
        )

    @action(detail=False, methods=['get'])
    def estadisticas(self, request):
        """Obtener estadísticas de citas"""
        hoy = timezone.now().date()
        
        total_citas = Cita.objects.count()
        citas_hoy = Cita.objects.filter(fecha=hoy).count()
        citas_agendadas = Cita.objects.filter(estado='Agendada').count()
        citas_confirmadas = Cita.objects.filter(estado='Confirmada').count()
        citas_canceladas = Cita.objects.filter(estado='Cancelada').count()
        citas_completadas = Cita.objects.filter(estado='Completada').count()
        
        return Response({
            'total_citas': total_citas,
            'citas_hoy': citas_hoy,
            'citas_agendadas': citas_agendadas,
            'citas_confirmadas': citas_confirmadas,
            'citas_canceladas': citas_canceladas,
            'citas_completadas': citas_completadas
        })
