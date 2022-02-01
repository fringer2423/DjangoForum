from django.shortcuts import render
from rest_framework import viewsets
from .models import Checkbox
from .serializers import CheckboxSerializers


class CheckboxViewset(viewsets.ModelViewSet):
    queryset = Checkbox.objects.all()
    serializer_class = CheckboxSerializers
