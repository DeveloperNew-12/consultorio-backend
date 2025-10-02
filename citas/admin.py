from django.contrib import admin
from .models import Cita

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('idcita', 'paciente', 'odontologo', 'fecha', 'horarioini', 'horafin', 'estado', 'motivo')
    search_fields = ('idcita', 'paciente__nombres', 'odontologo__nombre')
    list_filter = ('estado', 'fecha', 'canalrecordatorio')

# Register your models here.