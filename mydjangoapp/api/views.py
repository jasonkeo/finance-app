from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import viewsets
from .models import News
from .serializer import NewsSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
