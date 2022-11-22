from django.shortcuts import render
from rest_framework import viewsets
from api.models import Students
from api.serializers import StudentSerializers
# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializers