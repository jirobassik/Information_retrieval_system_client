from django.urls import path
from . import views

urlpatterns = [
    path('', views.metrics, name="metrics")
]
