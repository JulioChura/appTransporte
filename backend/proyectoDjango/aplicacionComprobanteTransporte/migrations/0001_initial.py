# Generated by Django 5.0.6 on 2024-07-22 11:04

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conductor',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=155)),
                ('surName', models.CharField(max_length=155)),
                ('DNI', models.IntegerField(blank=True, default=0, null=True)),
                ('adress', models.CharField(max_length=155)),
                ('phoneNumber', models.IntegerField(blank=True, default=0, null=True)),
                ('licenseType', models.CharField(max_length=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['name', 'surName', 'DNI'],
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Ruc', models.IntegerField()),
                ('Name', models.CharField(max_length=100)),
                ('Adress', models.CharField(max_length=255)),
                ('Contact', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=155)),
                ('license_plate', models.CharField(max_length=155)),
                ('seats', models.IntegerField()),
                ('year', models.IntegerField(blank=True, null=True)),
                ('operational', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['license_plate', 'year', 'model'],
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('DNI', models.IntegerField()),
                ('Cellphone', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('id_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clientes', to='aplicacionComprobanteTransporte.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('startingPlace', models.CharField(max_length=155)),
                ('destinationPlace', models.CharField(max_length=155)),
                ('distance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stops', models.IntegerField(blank=True, default=0, null=True)),
                ('horario', models.TimeField()),
                ('fecha', models.DateField()),
                ('cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('drivers', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rutas', to='aplicacionComprobanteTransporte.conductor')),
                ('vehicles', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rutas', to='aplicacionComprobanteTransporte.vehiculo')),
            ],
            options={
                'ordering': ['startingPlace', 'destinationPlace', 'distance', 'horario', 'fecha'],
            },
        ),
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vouchers', to='aplicacionComprobanteTransporte.cliente')),
                ('ruta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacionComprobanteTransporte.ruta')),
            ],
        ),
    ]
