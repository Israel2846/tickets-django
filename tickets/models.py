from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class UsuarioManager(BaseUserManager):
    def create_user(self, nombres_usuario, appat_usuario, apmat_usuario, num_empleado, num_tel, email, rol = None, password = None):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')
        
        usuario = self.model(
            nombres_usuario = nombres_usuario,
            appat_usuario = appat_usuario,
            apmat_usuario = apmat_usuario,
            num_empleado = num_empleado,
            num_tel = num_tel,
            email = self.normalize_email(email),
            rol = rol
        )

        usuario.set_password(password)
        usuario.save()
        return usuario
    
    def create_superuser(self, nombres_usuario, appat_usuario, apmat_usuario, num_empleado, num_tel, email, password):
        usuario = self.create_user(
            nombres_usuario = nombres_usuario,
            appat_usuario = appat_usuario,
            apmat_usuario = apmat_usuario,
            num_empleado = num_empleado,
            num_tel = num_tel,
            email = email, 
            rol = 1,
            password = password,
        )

        usuario.usuario_administrador = True
        usuario.save()
        return usuario


class Usuario(AbstractBaseUser):
    OPCIONES_ROL = (
        (2, 'Soporte'),
        (3, 'Usuario'),
    )
    nombres_usuario = models.CharField('Nombre(s)', max_length=200)
    appat_usuario = models.CharField('Apellido paterno', max_length=50)
    apmat_usuario = models.CharField('Apellido materno', max_length=50)
    num_empleado = models.IntegerField('Número de empleado', unique=True)
    num_tel = models.BigIntegerField('Número telefónico')
    email = models.EmailField('Correo electrónico', unique=True, max_length=254)
    rol = models.IntegerField('Rol', choices=OPCIONES_ROL)
    usuario_activo = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'num_empleado'
    REQUIRED_FIELDS = ['nombres_usuario', 'appat_usuario', 'apmat_usuario', 'num_tel', 'email']

    def __str__(self):
        return f'Usuario: {self.nombres_usuario} {self.appat_usuario} {self.apmat_usuario}'
    
    def has_perm(self,perm,obj = None):
        return True
    
    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
        return self.usuario_administrador
    

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