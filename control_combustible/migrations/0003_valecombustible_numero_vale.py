# Generated by Django 5.1.4 on 2025-01-09 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_combustible', '0002_alter_aeronave_capacidad_alter_aeronave_modelo'),
    ]

    operations = [
        migrations.AddField(
            model_name='valecombustible',
            name='numero_vale',
            field=models.IntegerField(default=0),
        ),
    ]