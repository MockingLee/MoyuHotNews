from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from django.urls import include

urlpatterns = [
    path('typelist', views.getTypeNews)
]