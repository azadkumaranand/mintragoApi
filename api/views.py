from django.shortcuts import render
from rest_framework import viewsets
from api.models import LabDress, Cycle
from api.serializers import DressSerializers, CycleSerializers
# Create your views here.

class DressViewSet(viewsets.ModelViewSet):
    queryset = LabDress.objects.all()
    serializer_class = DressSerializers

class CycleViewSet(viewsets.ModelViewSet):
    queryset = Cycle.objects.all()
    serializer_class = CycleSerializers