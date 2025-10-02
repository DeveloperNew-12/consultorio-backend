from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Rol, Usuario, UsuarioRol, SesionUsuario
from .serializers import RolSerializer, UsuarioSerializer, UsuarioRolSerializer, SesionUsuarioSerializer

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def create(self, request, *args, **kwargs):
        # Crear una copia mutable de los datos
        data = request.data.copy()
        
        # Encriptar contraseña antes de guardar
        if 'contrasena' in data and data['contrasena']:
            data['contrasena'] = make_password(data['contrasena'])
        
        # Crear el serializer con los datos modificados
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        # Crear una copia mutable de los datos
        data = request.data.copy()
        
        # Encriptar contraseña si se está actualizando y no está vacía
        if 'contrasena' in data and data['contrasena']:
            data['contrasena'] = make_password(data['contrasena'])
        elif 'contrasena' in data and not data['contrasena']:
            # Si la contraseña está vacía, no la actualizar
            data.pop('contrasena')
        
        # Obtener la instancia
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        
        # Crear el serializer con los datos modificados
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
            
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def activos(self, request):
        usuarios_activos = Usuario.objects.filter(estado='ACTIVO')
        serializer = self.get_serializer(usuarios_activos, many=True)
        return Response(serializer.data)

    def get_tokens_for_user(self, usuario):
        """Generar tokens JWT para el usuario personalizado"""
        refresh = RefreshToken()
        refresh['user_id'] = usuario.idusuario
        refresh['username'] = usuario.username
        refresh['nombre'] = usuario.nombre
        
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    @action(detail=False, methods=['post'])
    def login(self, request):
        """Login personalizado para usuarios del sistema"""
        username = request.data.get('username')
        contrasena = request.data.get('contrasena')
        
        if not username or not contrasena:
            return Response(
                {'error': 'Usuario y contraseña son requeridos'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            usuario = Usuario.objects.get(username=username, estado='ACTIVO')
            if check_password(contrasena, usuario.contrasena):
                # Actualizar último login
                usuario.ultimologin = timezone.now()
                usuario.save()
                
                # Crear sesión
                sesion = SesionUsuario.objects.create(usuario=usuario)
                
                # Generar tokens JWT
                tokens = self.get_tokens_for_user(usuario)
                
                serializer = self.get_serializer(usuario)
                return Response({
                    'usuario': serializer.data,
                    'sesion_id': sesion.id,
                    'access': tokens['access'],
                    'refresh': tokens['refresh'],
                    'mensaje': 'Login exitoso'
                })
            else:
                return Response(
                    {'error': 'Credenciales inválidas'}, 
                    status=status.HTTP_401_UNAUTHORIZED
                )
        except Usuario.DoesNotExist:
            return Response(
                {'error': 'Usuario no encontrado'}, 
                status=status.HTTP_404_NOT_FOUND
            )

    @action(detail=False, methods=['post'])
    def logout(self, request):
        """Logout personalizado"""
        sesion_id = request.data.get('sesion_id')
        
        if sesion_id:
            try:
                sesion = SesionUsuario.objects.get(id=sesion_id, fin_sesion__isnull=True)
                sesion.fin_sesion = timezone.now()
                sesion.save()
                return Response({'mensaje': 'Logout exitoso'})
            except SesionUsuario.DoesNotExist:
                return Response(
                    {'error': 'Sesión no encontrada'}, 
                    status=status.HTTP_404_NOT_FOUND
                )
        return Response(
            {'error': 'ID de sesión requerido'}, 
            status=status.HTTP_400_BAD_REQUEST
        )

    @action(detail=True, methods=['post'])
    def cambiar_estado(self, request, pk=None):
        """Cambiar estado de usuario (ACTIVO/INACTIVO)"""
        usuario = self.get_object()
        nuevo_estado = request.data.get('estado')
        
        if nuevo_estado in ['ACTIVO', 'INACTIVO']:
            usuario.estado = nuevo_estado
            usuario.save()
            serializer = self.get_serializer(usuario)
            return Response({
                'mensaje': f'Estado cambiado a {nuevo_estado}',
                'usuario': serializer.data
            })
        return Response(
            {'error': 'Estado inválido'}, 
            status=status.HTTP_400_BAD_REQUEST
        )

    @action(detail=True, methods=['post'])
    def cambiar_contrasena(self, request, pk=None):
        """Cambiar contraseña de usuario"""
        usuario = self.get_object()
        nueva_contrasena = request.data.get('nueva_contrasena')
        contrasena_actual = request.data.get('contrasena_actual')
        
        if not nueva_contrasena:
            return Response(
                {'error': 'Nueva contraseña es requerida'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Verificar contraseña actual si se proporciona
        if contrasena_actual and not check_password(contrasena_actual, usuario.contrasena):
            return Response(
                {'error': 'Contraseña actual incorrecta'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Cambiar contraseña
        usuario.contrasena = make_password(nueva_contrasena)
        usuario.save()
        
        return Response({
            'mensaje': 'Contraseña cambiada exitosamente'
        })

class UsuarioRolViewSet(viewsets.ModelViewSet):
    queryset = UsuarioRol.objects.all()
    serializer_class = UsuarioRolSerializer

class SesionUsuarioViewSet(viewsets.ModelViewSet):
    queryset = SesionUsuario.objects.all()
    serializer_class = SesionUsuarioSerializer
