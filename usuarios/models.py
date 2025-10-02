from django.db import models

class Rol(models.Model):
    idrol = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=150)
    correo = models.EmailField(unique=True, null=True, blank=True)
    contrasena = models.CharField(max_length=128, null=True, blank=True)  # aquí guardas la contraseña en texto cifrado o plano
    estado = models.CharField(
        max_length=10,
        choices=[('ACTIVO', 'Activo'), ('INACTIVO', 'Inactivo')],
        default='ACTIVO'
    )
    ultimologin = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.username})"


class UsuarioRol(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('usuario', 'rol')

    def __str__(self):
        return f"{self.usuario.nombre} - {self.rol.nombre}"


class SesionUsuario(models.Model):
    id = models.BigAutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    inicio_sesion = models.DateTimeField(auto_now_add=True)
    fin_sesion = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Sesión de {self.usuario.nombre} iniciada en {self.inicio_sesion}"  # pylint: disable=no-member
