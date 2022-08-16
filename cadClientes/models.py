from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_cliente = models.IntegerField(primary_key=True, serialize=True)
    nome_cliente = models.CharField(max_length=100)
    contato_cliente = models.CharField(max_length=20)




