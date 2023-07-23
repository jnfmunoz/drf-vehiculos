from django.urls import path
from . import views

urlpatterns = [
    path('add', views.new_vehiculo, name="new_vehiculo"),
    path('list', views.list_vehiculo, name="list_vehiculo"),
]