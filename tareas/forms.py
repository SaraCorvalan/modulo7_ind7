from django import forms
from .models import registroTareas
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class registroForm(forms.ModelForm):
    
    class Meta:
        fecha_vencimiento_tarea = forms.DateField(widget=forms.DateInput(format='%d-%m-%Y'))
        model = registroTareas
        fields = ('id_tarea', 
                    'titulo_tarea', 
                    'descripcion_tarea', 
                    'fecha_vencimiento_tarea', 
                    'categoria_tarea', 
                    'estado_tarea', 
                    'observaciones_tarea')



class LoginForm(forms.Form):
    usuario = forms.CharField(max_length=50, required=True, 
        label="Nombre de usuario", 
        error_messages={'required': 'Su nombre es requerido'})
    password = forms.CharField(widget=forms.PasswordInput, 
        max_length=20, required=True, 
        label="Contraseña", 
        error_messages={'required': 'Contraseña es obligatoria'})


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'groups', 'password1', 'password2']