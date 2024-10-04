# myapp/serializers.py
from rest_framework import serializers
from .models import News, Monthly

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['date', 'news', 'index']

class MonthlySerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['date', 'market_data']
