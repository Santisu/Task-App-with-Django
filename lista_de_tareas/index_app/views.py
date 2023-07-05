from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from task_app.models import Task, Label

class IndexView(View):
    def get(self, request):
        return render(request, "index.html", {})

@method_decorator(login_required, name ='dispatch')
class IndexUserView(View):

    labels = Label.objects.all()

    def dispatch(self, request, *args, **kwargs):
        self.usuario = request.user
        self.completed_tasks = Task.objects.filter(user_id=self.usuario.id, status='Completada').order_by('due_date')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        tasks = Task.objects.filter(user_id=self.usuario.id).exclude(status='Completada').order_by('due_date')
        context = {"tasks" : tasks, "labels" : self.labels}
        return render(request, "index_user.html", context)