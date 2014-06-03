from django.forms import ModelForm
from django import forms
from fixture.models import Seleccion, Partido, Grupo
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



	'''def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)
		user.set_email = (self.cleaned_data["mail"])
		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user'''

	'''def save(self, commit=True):
        #Cometando
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
        	user.save()
        return user'''