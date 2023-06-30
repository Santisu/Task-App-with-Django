from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.contrib.auth.models import User
from .models import Task, Label
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name ='dispatch')
class TaskListView(View):
    template = "tasks_list.html"
    
    def get(self, request):
        user = request.user
        labels = Label.objects.all()
        tasks = Task.objects.filter(user_id=user, status='Pendiente').order_by('due_date')
        context = {'tasks' : tasks,
                    'labels' : labels}
        return render(request, self.template, context)

@method_decorator(login_required, name ='dispatch')
class TaskItemView(View):
    template = "task_item.html"
    
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        labels = Label.objects.all()
        context = {'task' : task,
                    'labels' : labels}
        return render(request, self.template, context)
