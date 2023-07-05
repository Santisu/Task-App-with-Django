from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User

class LoginView(View):
    form = LoginForm()
    template_name = "login.html"

    def get(self, request):
        context = {"form": self.form}
        return render(request, self.template_name, context)
    def post(self, request):
        usuario = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if usuario is None:
            context = {"form": self.form,
                       'error': "El usuario o contraseña ingresada no son correctos"}
            return render(request, self.template_name, context)
        else:
            login(request, usuario)
            return redirect('index_user')

class RegisterView(View):
    form_class = RegisterForm
    template_name = "register.html"

    def get(self, request):
        form = self.form_class()
        context = {'form': form }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        print("Datos de request.POST:", request.POST)
        if form.is_valid():
            try:
                usuario = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'],
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    email=request.POST['email']
                )
                usuario.save()
                login(request, usuario)
                return redirect('index_user')
            except IntegrityError:
                context = {'form': form, 'error': "El nombre de usuario ya existe :("}
                return render(request, self.template_name, context)
        else:
            context = {'form': form}
            return render(request, self.template_name, context)



@login_required
def LogoutView(request):
    logout(request)
    return redirect('index')
