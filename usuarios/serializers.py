from rest_framework import serializers
from .models import Rol, Usuario, UsuarioRol, SesionUsuario

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'
        extra_kwargs = {
            'idrol': {'read_only': True}
        }

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        extra_kwargs = {
            'idusuario': {'read_only': True},
            'contrasena': {'write_only': True}
        }

class UsuarioRolSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioRol
        fields = '__all__'

class SesionUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = SesionUsuario
        fields = '__all__'
