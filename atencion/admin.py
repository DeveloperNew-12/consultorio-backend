from django.contrib import admin
from .models import Tratamiento, Consulta, Procedimiento

@admin.register(Tratamiento)
class TratamientoAdmin(admin.ModelAdmin):
    list_display = ('idtratamiento', 'nombre', 'preciobase')
    search_fields = ('nombre',)

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('idconsulta', 'paciente', 'odontologo', 'fecha', 'motivo', 'diagnostico')
    search_fields = ('idconsulta', 'paciente__nombres', 'odontologo__nombre')
    list_filter = ('fecha',)

@admin.register(Procedimiento)
class ProcedimientoAdmin(admin.ModelAdmin):
    list_display = ('idprocedimiento', 'consulta', 'tratamiento', 'cantidad', 'preciounitario', 'piezasafectadas')
    list_filter = ('tratamiento',)

# Register your models here.