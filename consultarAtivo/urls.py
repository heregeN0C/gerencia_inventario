from django.urls import path
from . import views

urlpatterns = [
    path('', views.consultarativo, name='index'),
    path('<int:cod_equipamento>', views.consultar_ativo_por_codigo, name='ver_contato'),
]
