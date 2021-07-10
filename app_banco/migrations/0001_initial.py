# Generated by Django 3.2.3 on 2021-07-09 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=20)),
                ('fecha_nacimiento', models.DateField()),
                ('telefono', models.IntegerField()),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Cuentas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creada', models.DateTimeField(auto_now_add=True)),
                ('estado', models.BooleanField(default=True)),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=15)),
                ('proprietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_banco.cliente')),
            ],
        ),
    ]