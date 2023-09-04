# Generated by Django 4.2.4 on 2023-09-03 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre de prioridad')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategoría',
            fields=[
                ('id_subcategoría', models.AutoField(primary_key=True, serialize=False, verbose_name='Id sugcategoría')),
                ('nombre_subCat', models.CharField(max_length=50, verbose_name='Nombre de subcategoría')),
                ('id_categoría', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.categoría')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id_ticket', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de ticket')),
                ('descripción', models.CharField(max_length=200, verbose_name='Descripción')),
                ('fecha_inicio', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de inicio')),
                ('fecha_fin', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de finalización')),
                ('tiempo_resolución', models.DurationField(blank=True, null=True)),
                ('documentos_adicionales', models.FileField(upload_to='documentos/')),
                ('id_categoría', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.categoría')),
                ('id_prioridad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.prioridad')),
                ('id_subcategoría', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.subcategoría')),
            ],
        ),
    ]