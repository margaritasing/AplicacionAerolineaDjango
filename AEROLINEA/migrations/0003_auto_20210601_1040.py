# Generated by Django 3.2.3 on 2021-06-01 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AEROLINEA', '0002_auto_20210601_1037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vuelo',
            name='destino',
        ),
        migrations.RemoveField(
            model_name='vuelo',
            name='origen',
        ),
        migrations.DeleteModel(
            name='Aeropuerto',
        ),
        migrations.DeleteModel(
            name='Vuelo',
        ),
    ]