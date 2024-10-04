from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import viewsets
from .models import News,Monthly
from .serializer import NewsSerializer,MonthlySerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class MonthlyViewSet(viewsets.ModelViewSet):
    queryset = Monthly.objects.all()
    serializer_class = MonthlySerializer

