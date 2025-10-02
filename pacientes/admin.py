from django.contrib import admin
from .models import Paciente, HistoriaClinica, Odontograma, PiezaDental, Adjunto

# ---------------- PACIENTE ----------------
@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('idpaciente', 'nombres', 'ci', 'sexo', 'telefono', 'correo')
    search_fields = ('idpaciente', 'nombres', 'ci', 'correo')
    list_filter = ('sexo',)


# ---------------- HISTORIA CLÍNICA ----------------
@admin.register(HistoriaClinica)
class HistoriaClinicaAdmin(admin.ModelAdmin):
    list_display = ('idhistoria', 'paciente_id_str', 'fechaapertura', 'observacionesgenerales')
    search_fields = ('idhistoria', 'paciente__idpaciente', 'paciente__nombres')

    def paciente_id_str(self, obj):
        return obj.paciente.idpaciente
    paciente_id_str.short_description = "IDPACIENTE"


# ---------------- ODONTOGRAMA ----------------
@admin.register(Odontograma)
class OdontogramaAdmin(admin.ModelAdmin):
    list_display = ('idodontograma', 'historia_id_str', 'fechacreacion', 'notas')

    def historia_id_str(self, obj):
        return obj.historia.idhistoria
    historia_id_str.short_description = "IDHISTORIA"


# ---------------- PIEZA DENTAL ----------------
@admin.register(PiezaDental)
class PiezaDentalAdmin(admin.ModelAdmin):
    list_display = ('idpieza', 'codigofdi', 'estado', 'odontograma_id_str')
    list_filter = ('estado',)

    def odontograma_id_str(self, obj):
        return obj.odontograma.idodontograma
    odontograma_id_str.short_description = "IDODONTOGRAMA"


# ---------------- ADJUNTO ----------------
@admin.register(Adjunto)
class AdjuntoAdmin(admin.ModelAdmin):
    list_display = ('idadjunto', 'tipo', 'rutaarchivo', 'fecha', 'historia_id_str')
    search_fields = ('idadjunto', 'tipo', 'historia__idhistoria')

    def historia_id_str(self, obj):
        return obj.historia.idhistoria
    historia_id_str.short_description = "IDHISTORIA"