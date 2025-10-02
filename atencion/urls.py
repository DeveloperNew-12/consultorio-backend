from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'tratamientos', views.TratamientoViewSet)
router.register(r'consultas', views.ConsultaViewSet)
router.register(r'procedimientos', views.ProcedimientoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
