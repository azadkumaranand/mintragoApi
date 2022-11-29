
from django.contrib import admin
from django.urls import path, include
from api.views import DressViewSet, CycleViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'dress', DressViewSet)
router.register(r'cycle', CycleViewSet)

urlpatterns = [
    path('', include(router.urls))
]
