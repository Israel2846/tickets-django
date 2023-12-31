# Generated by Django 4.2.5 on 2023-10-05 03:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nombres_usuario', models.CharField(max_length=200, verbose_name='Nombre(s)')),
                ('appat_usuario', models.CharField(max_length=50, verbose_name='Apellido paterno')),
                ('apmat_usuario', models.CharField(max_length=50, verbose_name='Apellido materno')),
                ('num_empleado', models.IntegerField(unique=True, verbose_name='Número de empleado')),
                ('num_tel', models.BigIntegerField(verbose_name='Número telefónico')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo electrónico')),
                ('rol', models.IntegerField(choices=[(2, 'Soporte'), (3, 'Usuario')], verbose_name='Rol')),
                ('usuario_activo', models.BooleanField(default=True)),
                ('usuario_administrador', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Categoría',
            fields=[
                ('id_categoría', models.AutoField(primary_key=True, serialize=False, verbose_name='Id categoría')),
                ('nombre_cat', models.CharField(max_length=50, verbose_name='Nombre de categoría')),
            ],
        ),
        migrations.CreateModel(
            name='Prioridad',
            fields=[
                ('id_prioridad', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de prioridad')),
                ('nombre_prioridad', models.CharField(max_length=50, verbose_name='Nombre de prioridad')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategoría',
            fields=[
                ('id_subcategoría', models.AutoField(primary_key=True, serialize=False, verbose_name='Id subcategoría')),
                ('nombre_subCat', models.CharField(max_length=50, verbose_name='Nombre de subcategoría')),
                ('id_categoría', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.categoría')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id_ticket', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de ticket')),
                ('descripción', models.TextField(verbose_name='Descripción')),
                ('fecha_inicio', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de inicio')),
                ('fecha_fin', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de finalización')),
                ('tiempo_resolución', models.DurationField(blank=True, null=True)),
                ('documentos_adicionales', models.FileField(blank=True, upload_to='documentos/')),
                ('estado', models.IntegerField(choices=[(1, 'Abierto'), (2, 'En Progreso'), (3, 'Completado'), (4, 'Pausado')], default=1, verbose_name='Estado')),
                ('id_categoría', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.categoría', verbose_name='Categoría')),
                ('id_prioridad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.prioridad', verbose_name='Prioridad')),
                ('id_subcategoría', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.subcategoría', verbose_name='Subcategoría')),
                ('usuario_creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
