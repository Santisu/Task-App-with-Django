from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Nombre de usuario"
        self.fields['password'].label = 'Contraseña'

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'

class RegisterForm(UserCreationForm):

        def __init__(self, *args, **kwargs):
            super(RegisterForm, self).__init__(*args, **kwargs)
            self.fields['username'].label = 'Nombre de usuario'
            self.fields['password1'].label = 'Contraseña'
            self.fields['password2'].label = 'Confirmar contraseña'
            self.fields['first_name'].label = 'Nombre'
            self.fields['last_name'].label = 'Apellido'
            self.fields['email'].label = 'Correo electronico'

            self.fields['username'].widget.attrs['class'] = 'form-control'
            self.fields['password1'].widget.attrs['class'] = 'form-control'
            self.fields['password2'].widget.attrs['class'] = 'form-control'
            self.fields['first_name'].widget.attrs['class'] = 'form-control'
            self.fields['last_name'].widget.attrs['class'] = 'form-control'
            self.fields['email'].widget.attrs['class'] = 'form-control'

        
        first_name = forms.CharField(max_length=30)
        last_name = forms.CharField(max_length=30)
        email = forms.EmailField()

        class Meta:
            model = User
            fields = UserCreationForm.Meta.fields
