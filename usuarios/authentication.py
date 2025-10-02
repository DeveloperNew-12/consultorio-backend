# usuarios/authentication.py
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from django.contrib.auth.models import AnonymousUser
from .models import Usuario

class CustomJWTAuthentication(JWTAuthentication):
    """
    Autenticación JWT personalizada para trabajar con nuestro modelo Usuario personalizado
    """
    
    def get_user(self, validated_token):
        """
        Attempts to find and return a user using the given validated token.
        """
        try:
            user_id = validated_token.get('user_id')
        except KeyError:
            raise InvalidToken('Token contained no recognizable user identification')

        try:
            user = Usuario.objects.get(idusuario=user_id, estado='ACTIVO')
        except Usuario.DoesNotExist:
            raise InvalidToken('User not found')

        return user

    def authenticate(self, request):
        """
        Returns a two-tuple of `User` and token if a valid signature has been
        supplied using JWT-based authentication.  Otherwise returns `None`.
        """
        header = self.get_header(request)
        if header is None:
            return None

        raw_token = self.get_raw_token(header)
        if raw_token is None:
            return None

        validated_token = self.get_validated_token(raw_token)
        user = self.get_user(validated_token)

        return user, validated_token
