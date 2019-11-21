from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views

router = DefaultRouter()
router.register('servicios', views.ServicioViewSet , base_name='servicios')

urlpatterns = router.urls


