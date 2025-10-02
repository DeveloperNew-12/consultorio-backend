from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'pacientes', views.PacienteViewSet)
router.register(r'historias', views.HistoriaClinicaViewSet)
router.register(r'odontogramas', views.OdontogramaViewSet)
router.register(r'piezas', views.PiezaDentalViewSet)
router.register(r'adjuntos', views.AdjuntoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
