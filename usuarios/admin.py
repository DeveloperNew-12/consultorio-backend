from django.contrib import admin
from .models import Usuario, UsuarioRol, Rol, SesionUsuario

@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ('idrol', 'nombre', 'descripcion')
    search_fields = ('nombre',)


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('idusuario', 'nombre', 'correo', 'estado', 'ultimologin')
    search_fields = ('nombre', 'correo')
    list_filter = ('estado',)


@admin.register(UsuarioRol)
class UsuarioRolAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'rol')
    list_filter = ('rol',)


@admin.register(SesionUsuario)
class SesionUsuarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'inicio_sesion', 'fin_sesion')
    list_filter = ('inicio_sesion',)
