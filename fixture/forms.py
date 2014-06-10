from django.forms import ModelForm
from django import forms
from fixture.models import Seleccion, Partido, Grupo, Resultado
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactoForm (forms.Form):
	correo = forms.EmailField(label = 'Tu correo electronico')
	mensaje = forms.CharField (widget=forms.Textarea)


class UserRegisterForm(UserCreationForm):
	
	username = forms.RegexField(label=("Usuario"), max_length=30,
        regex=r'^[\w.@+-]+$',
        error_messages={
            'invalid': ("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")})
	password1 = forms.CharField(label=("Clave"),widget=forms.PasswordInput)
	password2 = forms.CharField(label=("Confirmar clave"),widget=forms.PasswordInput)
	
	class Meta:
		model = User
		fields = ("username","first_name", "last_name", "email",)


class ResultadoForm (ModelForm):
	e1_goles = forms.IntegerField(widget=forms.TextInput(attrs={'size':2, 'id':'goles1', 'class': 'goles loc', 'onchange':'anotarResultado(this)', 'onselect':'cambioInput(this)', 'onclick':'cambioInput(this)'}))
	e2_goles = forms.IntegerField(widget=forms.TextInput(attrs={'size':2, 'id':'goles2', 'class': 'goles vis', 'onselect':'cambioInput(this)', 'onclick':'cambioInput(this)'}))

	class Meta:
		model  = Resultado

