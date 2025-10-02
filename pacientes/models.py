from django.db import models

class Paciente(models.Model):
    SEXOS = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]

    idpaciente = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=150)
    ci = models.CharField(max_length=20, unique=True)
    fechanacimiento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SEXOS)
    direccion = models.TextField(null=True, blank=True)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    alergias = models.TextField(null=True, blank=True)
    antecedentes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.idpaciente} - {self.nombres}"


class HistoriaClinica(models.Model):
    idhistoria = models.CharField(primary_key=True, max_length=20)
    fechaapertura = models.DateField()
    observacionesgenerales = models.TextField(null=True, blank=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.idhistoria} - {self.paciente.nombres}" # pylint: disable=no-member


class Odontograma(models.Model):
    idodontograma = models.CharField(primary_key=True, max_length=20)
    fechacreacion = models.DateField()
    notas = models.TextField(null=True, blank=True)
    historia = models.ForeignKey(HistoriaClinica, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.idodontograma} ({self.historia.idhistoria})" # pylint: disable=no-member


class PiezaDental(models.Model):
    ESTADOS = [
        ('Sana','Sana'),
        ('Caries','Caries'),
        ('Tratada','Tratada'),
        ('En tratamiento','En tratamiento'),
        ('Extraída','Extraída')
    ]

    idpieza = models.CharField(primary_key=True, max_length=20)
    codigofdi = models.CharField(max_length=2)
    estado = models.CharField(max_length=20, choices=ESTADOS)
    observacion = models.TextField(null=True, blank=True)
    odontograma = models.ForeignKey(Odontograma, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.idpieza} - {self.estado}"

class Adjunto(models.Model):
    idadjunto = models.CharField(primary_key=True, max_length=20)
    tipo = models.CharField(max_length=50)
    rutaarchivo = models.CharField(max_length=255)
    fecha = models.DateField()
    descripcion = models.TextField(null=True, blank=True)
    historia = models.ForeignKey(HistoriaClinica, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.idadjunto} ({self.tipo})"