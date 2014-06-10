#encoding:utf-8

from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django import forms

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
    def __unicode__(self):
    	return str(self.usuario)

class Estadio (models.Model):
	nombre = models.CharField(max_length=40)
	dimensiones = models.CharField(max_length=40)
	capacidad = models.IntegerField()
	apertura = models.IntegerField(max_length=4)
	foto = models.ImageField(upload_to='images/estadio', verbose_name='Foto Estadio')
	def __unicode__(self):
		return self.nombre

class Jugador (models.Model):
	nombre = models.CharField(max_length=40)
	apodo = models.CharField(max_length=15, blank=True)
	nacimiento = models.DateField()
	debut = models.IntegerField(max_length=4)
	goles_seleccion = models.IntegerField(max_length=4)
	goles = models.IntegerField(max_length=4)
	foto = models.ImageField(upload_to='images/jugador', verbose_name='Foto Perfil')

	def __unicode__(self):
		return self.nombre

class Tecnico (models.Model):
	nombre = models.CharField(max_length=40)
	apodo = models.CharField(max_length=15, blank = True)
	nacimiento = models.DateField()
	titulos = models.IntegerField(max_length=4)
	foto = models.ImageField(upload_to='images/tecnico', verbose_name='Foto Perfil')
	def __unicode__(self):
		return self.nombre

class Seleccion (models.Model):
	pais = models.CharField(max_length=40, unique=True)
	cod_fifa = models.CharField(max_length=3)
	tecnico =  models.ForeignKey(Tecnico)
	goleador =  models.ForeignKey(Jugador, related_name='goleador')
	mas_partidos = models.ForeignKey(Jugador, related_name='mas participaciones')
	ranking_fifa = models.IntegerField(max_length=3, verbose_name='Ranking')
	mejor_lugar = models.IntegerField(max_length=3)
	mejor_lugar_fecha = models.DateField()
	peor_lugar = models.IntegerField(max_length=3)
	peor_lugar_fecha = models.DateField()
	escudo = models.ImageField(upload_to='images/escudos', verbose_name='Escudo')
	bandera = models.ImageField(upload_to='images/banderas', verbose_name='Bandera')
	estadio = models.ForeignKey(Estadio)

	def escudo_image(self):
		return '<img src="http://127.0.0.1:8000/media/%s" width="30"/>' % self.escudo
	def bandera_image(self):
		return '<img src="http://127.0.0.1:8000/media/%s" width="50"/>' % self.bandera
	
	escudo_image.allow_tags = True
	bandera_image.allow_tags = True

	def __unicode__(self):
		return self.pais


class SeleccionAdmin (admin.ModelAdmin):
	list_display = ('pais', 'bandera_image', 'escudo_image', 'tecnico','ranking_fifa','estadio')
	search_fields = ('pais',)

class Partido (models.Model):
	fecha = models.DateTimeField()
	lugar = models.CharField(max_length=40)
	e1 = models.ForeignKey(Seleccion, related_name='seleccion_e1')
	e2 = models.ForeignKey(Seleccion, related_name='seleccion_e2')
	
	@property
	def getFecha(self):
		return '%s' % self.fecha.strftime('%d/%m %H:%M')

	def __unicode__(self):
		return '%s vs 	%s' % (self.e1, self.e2)

class Grupo (models.Model):
    letra = models.CharField(max_length=1, unique=True)
    e1 = models.ForeignKey(Seleccion, related_name='seleccion_equipo1')
    e2 = models.ForeignKey(Seleccion, related_name='seleccion_equipo2')
    e3 = models.ForeignKey(Seleccion, related_name='seleccion_equipo3')
    e4 = models.ForeignKey(Seleccion, related_name='seleccion_equipo4')
    p1 = models.ForeignKey(Partido, related_name='partido_partido1')
    p2 = models.ForeignKey(Partido, related_name='partido_partido2')
    p3 = models.ForeignKey(Partido, related_name='partido_partido3')
    p4 = models.ForeignKey(Partido, related_name='partido_partido4')
    p5 = models.ForeignKey(Partido, related_name='partido_partido5')
    p6 = models.ForeignKey(Partido, related_name='partido_partido6')
    def __unicode__(self):
        return 'Grupo '+ self.letra

class Resultado (models.Model):
	TIPO_RESULTADO = ((0, "Local"),(1, "Empate"),(2, "Visitante"))
	prode = models.ForeignKey(Prode)
	partido = models.ForeignKey(Partido)
	e1_goles = models.IntegerField(max_length=2)
	e2_goles = models.IntegerField()
	resultado = models.PositiveSmallIntegerField(choices = TIPO_RESULTADO)
	
	class Meta:
		verbose_name_plural = "Resultados de los Partidos"
	def __unicode__(self):
		return str(self.partido.fecha) + "  " + str(self.partido.e1) + " " + str(self.e1_goles) + " - " +str(self.partido.e2) + " " + str(self.e2_goles)+" / Ganador: " + str(self.ganador)

