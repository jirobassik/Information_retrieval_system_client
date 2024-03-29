from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name="search"),
    path('download_file/<int:pk>', views.download_file, name='file-download'),
    path('classification_file/<int:pk>', views.classification_text_file, name='file-class'),
]
