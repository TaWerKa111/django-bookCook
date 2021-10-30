from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('recipe/<int:pk>', views.recipe_detail, name='recipe_detail')
]
