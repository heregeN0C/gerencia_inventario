from django.urls import path
from . import views

#referências de urls para a seção pagInicial
urlpatterns = [
    path('', views.index)
]