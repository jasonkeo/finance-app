# myapp/serializers.py
from rest_framework import serializers
from .models import News

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['date', 'news', 'index','analysis']

