from django.db import models
from pacientes.models import Paciente, HistoriaClinica
from usuarios.models import Usuario
from citas.models import Cita

class Tratamiento(models.Model):
    idtratamiento = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    preciobase = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} ({self.idtratamiento})"


class Consulta(models.Model):
    idconsulta = models.CharField(primary_key=True, max_length=20)
    fecha = models.DateField()
    motivo = models.TextField()
    diagnostico = models.TextField(null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    odontologo = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    historia = models.ForeignKey(HistoriaClinica, on_delete=models.CASCADE)
    cita = models.OneToOneField(Cita, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.idconsulta} - {self.paciente.nombres}" # pylint: disable=no-member


class Procedimiento(models.Model):
    idprocedimiento = models.CharField(primary_key=True, max_length=20)
    cantidad = models.IntegerField()
    preciounitario = models.DecimalField(max_digits=12, decimal_places=2)
    piezasafectadas = models.TextField(null=True, blank=True)

    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    tratamiento = models.ForeignKey(Tratamiento, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.idprocedimiento} ({self.tratamiento.nombre})"  # pylint: disable=no-member


# Create your models here.
