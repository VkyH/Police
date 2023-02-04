from django.urls import path, include
from rest_framework import routers
from .views import PersonViewSet
from . import views
router = routers.DefaultRouter()
router.register('persons', PersonViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.index, name='index'),
    path('/upload', views.upload, name='upload'),
    path('/vni',views.vni, name='vni'),
]