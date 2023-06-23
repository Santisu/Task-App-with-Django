from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import LoginForm

# Create your views here.
class LoginView(View):
    form = LoginForm()
    def get(self, request):
        context = {"form": self.form}
        return render(request, 'login.html', context)
    def post(self, request):
        usuario = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if usuario is None:
            context = {"form": self.form,
                       'error': "El usuario o contraseña ingresada no son correctos"}
            return render(request, 'iniciar_sesion.html', context)
        else:
            login(request, usuario)
            return redirect('index_user')
        
@login_required
def LogoutView(request):
    logout(request)
    return redirect('index')

@method_decorator(login_required, name ='dispatch')
class IndexUserView(View):

    def get(self, request):
        return render(request, "index_user.html")
