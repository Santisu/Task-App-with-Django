from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.contrib.auth.models import User
from .models import Task, Label
from .forms import TaskFilterForm, TaskCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q

@method_decorator(login_required, name='dispatch')
class TaskListView(View):
    template = "tasks_list.html"
    labels = Label.objects.all()
    form = TaskFilterForm

    def get(self, request):
        usuario = request.user
        tasks = Task.objects.filter(Q(user_id=usuario.id, status='En Progreso') | Q(user_id=usuario.id, status='Pendiente')).order_by('due_date')
        context = {'tasks': tasks,
                   'labels': self.labels,
                   'form': self.form}
        return render(request, self.template, context)

    def post(self, request):
        usuario = request.user
        label = request.POST['label']
        if label == "all":
            filtered_tasks = Task.objects.filter(Q(user_id=usuario.id, status='En Progreso') | Q(user_id=usuario.id, status='Pendiente')).order_by('due_date')
        else:
            filtered_tasks = Task.objects.filter(Q(user_id=usuario.id, label=label, status='En Progreso') | Q(user_id=usuario.id, label=label , status='Pendiente')).order_by('due_date')
        
        context = {'tasks' : filtered_tasks,
                    'labels' : self.labels,
                    'form' : self.form}

        if label != "all":
            context['requested_label'] = int(label)

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

@method_decorator(login_required, name ='dispatch')
class TaskCreationView(View):
    template = "task_edit.html"


    def get(self, request):
        form = TaskCreationForm
        context = {'form' : form}
        return render(request, self.template, context)
    
    def post(self, request):
        form = TaskCreationForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user_id = request.user.id
            task.save()
            return redirect('tasks_list')
        context = {'form': form}
        return render(request, self.template, context)


# @method_decorator(login_required, name ='dispatch')
# class TaskEditionView(View):
#     template = "task_edit.html"

#     def get(self, request, pk):
#         task = get_object_or_404(Task, pk=pk)
#         labels = Label.objects.all()
#         context = {'task' : task,
#                     'labels' : labels}
#         return render(request, self.template, context)