from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views

router = DefaultRouter()
router.register('mesas', views.MesaViewSet , base_name='mesa')

urlpatterns = router.urls


