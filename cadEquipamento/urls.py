from django.urls import path
from . import views


urlpatterns = [
    path('', views.cadequipamento, name='cadequipamento'),
]