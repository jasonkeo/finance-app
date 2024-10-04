# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewsViewSet,MonthlyViewSet

router = DefaultRouter()
router.register(r'news', NewsViewSet)
router.register(r'monthly', MonthlyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
