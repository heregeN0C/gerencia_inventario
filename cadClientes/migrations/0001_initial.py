# Generated by Django 4.1 on 2022-08-16 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.IntegerField(primary_key=True, serialize=False)),
                ('nome_cliente', models.CharField(max_length=100)),
                ('contato_cliente', models.CharField(max_length=20)),
            ],
        ),
    ]
