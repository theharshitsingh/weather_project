from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('city_weather/', views.city_weather, name='city_weather'),
]

