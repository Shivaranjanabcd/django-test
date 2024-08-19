from django.shortcuts import render
from rest_framework import generics
from .serializers import appserializer
from myapp.models import app
class app_api(generics.ListCreateAPIView):
    queryset = app.objects.all()
    serializer_class = appserializer
    
class RUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = app.objects.all()
    serializer_class = appserializer
    lookup_field = "pk"    