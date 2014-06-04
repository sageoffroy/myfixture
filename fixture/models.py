#encoding:utf-8

from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=80)
    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group_id = models.IntegerField()
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        managed = False
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    group = models.ForeignKey(AuthGroup)
    class Meta:
        managed = False
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user_id = models.IntegerField()
    content_type_id = models.IntegerField(blank=True, null=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    class Meta:
        managed = False
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(unique=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'django_session'

# Create your models here.
class Prode (models.Model):
    usuario = models.ForeignKey(User)
    class Meta:
        verbose_name_plural = "Prode de los usuarios"

class Seleccion (models.Model):
	pais = models.CharField(max_length=40, unique=True)
	tecnico = models.CharField(max_length=80)
	escudo = models.ImageField(upload_to='images/escudos', verbose_name='Imagen')

	def escudo_image(self):
		return '<img src="http://127.0.0.1:8000/media/%s"/>' % self.escudo
	escudo_image.allow_tags = True

	def __unicode__(self):
		return self.pais


class SeleccionAdmin (admin.ModelAdmin):
	list_display = ('pais','tecnico','escudo_image')
	search_fields = ('pais',)

class Grupo (models.Model):
    letra = models.CharField(max_length=1, unique=True)
    equipo1 = models.ForeignKey(Seleccion, related_name='seleccion_equipo1')
    equipo2 = models.ForeignKey(Seleccion, related_name='seleccion_equipo2')
    equipo3 = models.ForeignKey(Seleccion, related_name='seleccion_equipo3')
    equipo4 = models.ForeignKey(Seleccion, related_name='seleccion_equipo4')

    def __unicode__(self):
        return 'Grupo '+ self.letra

class Partido (models.Model):
	fecha = models.DateField()
	e1 = models.ForeignKey(Seleccion, related_name='seleccion_e1')
	e2 = models.ForeignKey(Seleccion, related_name='seleccion_e2')


class Resultado (models.Model):
    prode = models.ForeignKey(Prode)
    partido = models.ForeignKey(Partido)
    e1_goles = models.IntegerField()
    e2_goles = models.IntegerField()
    ganador = models.ForeignKey(Seleccion, related_name='seleccion_ganador')
    empate = models.BooleanField()
    class Meta:
        verbose_name_plural = "Resultados de los Partidos"
