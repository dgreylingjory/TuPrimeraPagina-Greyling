# Generated by Django 5.1.4 on 2025-01-09 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_combustible', '0004_alter_valecombustible_despachador_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valecombustible',
            name='fecha',
            field=models.DateField(),
        ),
    ]