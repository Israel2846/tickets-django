from django.db import models
from django.utils import timezone

# Create your models here.
class Categoría(models.Model):
    id_categoría = models.AutoField(verbose_name='Id categoría', primary_key=True)
    nombre_cat = models.CharField(verbose_name='Nombre de categoría', max_length=50)


class SubCategoría(models.Model):
    id_subcategoría = models.AutoField(verbose_name='Id sugcategoría', primary_key=True)
    id_categoría = models.ForeignKey(Categoría, on_delete=models.CASCADE)
    nombre_subCat = models.CharField(verbose_name='Nombre de subcategoría', max_length=50)


class Prioridad(models.Model):
    id_prioridad = models.AutoField(verbose_name='Id de prioridad', primary_key=True)
    nombre = models.CharField(verbose_name='Nombre de prioridad', max_length=50)


class Ticket(models.Model):
    id_ticket = models.AutoField(verbose_name='Id de ticket', primary_key=True)
    id_categoría = models.ForeignKey(Categoría, on_delete=models.CASCADE)
    id_subcategoría = models.ForeignKey(SubCategoría, on_delete=models.CASCADE)
    id_prioridad = models.ForeignKey(Prioridad, on_delete=models.CASCADE)
    descripción = models.CharField(verbose_name='Descripción', max_length=200)
    fecha_inicio = models.DateTimeField(verbose_name='Fecha de inicio', auto_now_add=True)
    fecha_fin = models.DateTimeField(verbose_name='Fecha de finalización', null=True, blank=True)
    tiempo_resolución = models.DurationField(null=True, blank=True)
    documentos_adicionales = models.FileField(upload_to='documentos/')

    def cerrar_tarea(self):
        if self.estado != 'cerrado':
            self.estado = 'cerrado'
            self.fecha_fin = timezone.now()
            self.duracion = self.fecha_fin - self.fecha_inicio  # Calcula la duración
            self.save()