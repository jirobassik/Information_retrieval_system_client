from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name="search"),
    path('delete_file/<int:pk>', views.delete_file, name='file-delete'),
    path('download_file/<int:pk>', views.download_file, name='file-download'),
]
