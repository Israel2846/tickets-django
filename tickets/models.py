from django.db import models
from django.utils import timezone

# Create your models here.
class Categoría(models.Model):
    id_categoría = models.AutoField(verbose_name='Id categoría', primary_key=True)
    nombre_cat = models.CharField(verbose_name='Nombre de categoría', max_length=50)

    def __str__(self) -> str:
        return self.nombre_cat


class SubCategoría(models.Model):
    id_subcategoría = models.AutoField(verbose_name='Id subcategoría', primary_key=True)
    id_categoría = models.ForeignKey(Categoría, on_delete=models.CASCADE)
    nombre_subCat = models.CharField(verbose_name='Nombre de subcategoría', max_length=50)

    def __str__(self) -> str:
        return self.nombre_subCat


class Prioridad(models.Model):
    id_prioridad = models.AutoField(verbose_name='Id de prioridad', primary_key=True)
    nombre_prioridad = models.CharField(verbose_name='Nombre de prioridad', max_length=50)

    def __str__(self) -> str:
        return self.nombre_prioridad


class Ticket(models.Model):
    ESTADO_CHOICES = (
        (1, 'Abierto'),
        (2, 'En Progreso'),
        (3, 'Completado'),
        (4, 'Pausado'),
    )
    id_ticket = models.AutoField(verbose_name='Id de ticket', primary_key=True)
    id_categoría = models.ForeignKey(Categoría, on_delete=models.CASCADE, verbose_name='Categoría')
    id_subcategoría = models.ForeignKey(SubCategoría, on_delete=models.CASCADE, verbose_name='Subcategoría')
    id_prioridad = models.ForeignKey(Prioridad, on_delete=models.CASCADE, verbose_name='Prioridad')
    descripción = models.TextField(verbose_name='Descripción')
    fecha_inicio = models.DateTimeField(verbose_name='Fecha de inicio', auto_now_add=True)
    fecha_fin = models.DateTimeField(verbose_name='Fecha de finalización', null=True, blank=True)
    tiempo_resolución = models.DurationField(null=True, blank=True)
    documentos_adicionales = models.FileField(upload_to='documentos/', blank=True)
    estado = models.IntegerField(verbose_name='Estado', choices=ESTADO_CHOICES, default=1)

    def cerrar_tarea(self):
        if self.estado != 3:
            self.estado = 3
            self.fecha_fin = timezone.now()
            self.duracion = self.fecha_fin - self.fecha_inicio  # Calcula la duración
            self.save()