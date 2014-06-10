from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect

#modelos propios
from fixture.models import Seleccion, Grupo, Partido
from fixture.forms import ContactoForm, UserRegisterForm, ResultadoForm

#Gestion de usuarios

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


def selecciones(request):
	selecciones = Seleccion.objects.all()
	return render_to_response('selecciones.html',{'selecciones':selecciones},context_instance=RequestContext(request))

def fixture(request):
	grupos = Grupo.objects.all()
	partidos = Partido.objects.all()

	if request.method == 'POST':
		form = ResultadoForm(request.POST)
		if form.is_valid:
			form.save()
			return HttpResponseRedirect('/fixture')
	else:
		form = ResultadoForm()
	return render_to_response('fixture.html',{'form':form, 'grupos':grupos},context_instance=RequestContext(request))


def home(request):
	selecciones = Seleccion.objects.all()
	return render_to_response('index.html',{'selecciones':selecciones},context_instance=RequestContext(request))

def contacto(request):
	if request.method == 'POST':
		formulario = ContactoForm(request.POST)
		if formulario.is_valid():
			titulo = 'Mnesaje desde el recetario'
			contenido = formlario.cleaned_data['mensaje']+"\n"
			contenido += 'Comunicarse a: ' + formulario.cleaned_data['correo']
			correro = EmailMesagge(titulos, contenido, to=['sageoffroy@gmail.com'])
			correo.send()
			return HttpResponseRedirect('/')
	else:
		formulario = ContactoForm()
	return render_to_response('contacto.html',{'formulario':formulario},context_instance=RequestContext(request))

def user_register (request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid:
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = UserRegisterForm()
	return render_to_response('register.html',{'form':form},context_instance=RequestContext(request))

def user_login (request):
	if request.method == 'POST':
		form = AuthenticationForm(request.POST)
		if form.is_valid:
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username=usuario, password=clave)
			if acceso is not None:
				if acceso.is_active:
					login(request,acceso)
					return HttpResponseRedirect('/')
				else:
					return HttpResponseRedirect('/')
			else:
				return HttpResponseRedirect('/')
		else:
			return HttpResponseRedirect('/')
	else:
		form = AuthenticationForm(request.POST)
	return render_to_response('index.html',{'form':form},context_instance=RequestContext(request))

@login_required(login_url='/')
def user_logout (request):
	logout(request)
	return HttpResponseRedirect('/')