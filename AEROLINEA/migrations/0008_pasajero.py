# Generated by Django 3.2.3 on 2021-06-01 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AEROLINEA', '0007_auto_20210601_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pasajero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('apellido', models.CharField(max_length=64)),
                ('vuelos', models.ManyToManyField(blank=True, related_name='pasajeros', to='AEROLINEA.Vuelo')),
            ],
        ),
    ]
