from django.db import models
from pacientes.models import Paciente
from usuarios.models import Usuario

class Cita(models.Model):
    ESTADOS = [
        ('Agendada','Agendada'),
        ('Completada','Completada'),
        ('Cancelada','Cancelada'),
        ('Confirmada','Confirmada'),
        ('No-Show','No-Show')
    ]
    CANALES = [
        ('SMS','SMS'),
        ('Email','Email'),
        ('WhatsApp','WhatsApp')
    ]

    idcita = models.AutoField(primary_key=True)
    fecha = models.DateField()
    horarioini = models.TimeField()
    horafin = models.TimeField()
    estado = models.CharField(max_length=15, choices=ESTADOS, default='Agendada')
    motivo = models.TextField()
    canalrecordatorio = models.CharField(max_length=20, choices=CANALES, null=True, blank=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    odontologo = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.idcita} - {self.paciente.nombres}"  # pylint: disable=no-member

# Create your models here.
