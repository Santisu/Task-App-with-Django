from datetime import datetime
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from .models import Priority, Task, Label, TaskObservation
from .forms import TaskFilterForm, TaskForm, ObservationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class TaskListView(View):

    """
     Shows the list of pending tasks.
     Post method filter the items acording to the parameters specified by user
    """

    template = "tasks_list.html"
    labels = Label.objects.all()
    form = TaskFilterForm
    prioritys = Priority.objects.all()

    def dispatch(self, request, *args, **kwargs):
        self.usuario = request.user
        self.completed_tasks = Task.objects.filter(user_id=self.usuario.id, status='Completada').order_by('due_date')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        tasks = Task.objects.filter(user_id=self.usuario.id).exclude(status='Completada').order_by('due_date')
        context = {'tasks': tasks,
                   'labels': self.labels,
                   'form': self.form,
                   'completed_tasks' : self.completed_tasks}
        return render(request, self.template, context)

    def post(self, request):
        label = request.POST['label']
        status = request.POST['status']
        priority = request.POST['priority']
        max_due = request.POST['max_due']

        if label == "all_tasks":
            filtered_tasks = Task.objects.filter(user_id=self.usuario.id).exclude(status='Completada').order_by('due_date')
        else:
            filtered_tasks = Task.objects.filter(user_id=self.usuario.id, label=label).exclude(status='Completada').order_by('due_date')

        if status == "all_status":
            pass
        else:
             filtered_tasks = filtered_tasks.filter(status=status)

        if priority == "all_priority":
            pass
        else:
             filtered_tasks = filtered_tasks.filter(priority=priority)

        if max_due:
            max_due = datetime.strptime(max_due, '%Y-%m-%d').date()
            filtered_tasks = filtered_tasks.filter(due_date__lt=max_due)

        context = {'tasks' : filtered_tasks,
                    'labels' : self.labels,
                    'form' : self.form,
                    'completed_tasks' : self.completed_tasks}

        if label != "all_tasks":
            context['requested_label'] = int(label)

        if priority != "all_priority":
            context['requested_priority'] = int(priority)
            context['priority'] = self.prioritys

        return render(request, self.template, context)


@method_decorator(login_required, name ='dispatch')
class TaskItemView(View):

    """
    Shows in a card a certain item requested by the user
    """

    template = "task_item.html"
    observation_form = ObservationForm
    
    def dispatch(self, request, *args, **kwargs):
        self.usuario = request.user
        self.task = get_object_or_404(Task, pk=kwargs['pk'])
        if self.task.user != self.usuario:
            return HttpResponseForbidden("No tienes permiso para acceder a esta tarea.")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        observations = TaskObservation.objects.filter(task_id=self.task.id)
        context = {'task' : self.task,
                    'observations' : observations,
                    'form' : self.observation_form}
        return render(request, self.template, context)
    
    def post(self, request, *args, **kwargs):
        if 'complete' in request.POST:
            self.task.status = 'Completada'
            self.task.save()
        elif 'delete_task' in request.POST:
            self.task.delete()
        elif "observation" in request.POST:
            form = self.observation_form(request.POST)
            if form.is_valid():
                observation = form.save(commit=False)
                observation.task = self.task
                observation.save()
                return redirect(request.get_full_path())
        elif "delete_observation" in request.POST:
            observation_id = request.POST.get('delete_observation')
            observation = get_object_or_404(TaskObservation, id=observation_id)
            observation.delete()
            return redirect(request.get_full_path())
        return redirect('tasks_list')


@method_decorator(login_required, name ='dispatch')
class TaskCreationView(View):

    """
    Create a new task object    
    """
    form = TaskForm
    template = "task_edit.html"
    title = "Agregar Tarea"

    def get(self, request):
        form = self.form
        context = {'form' : form,
                   'title' : self.title}
        return render(request, self.template, context)
    
    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks_list')
        context = {'form': form,
                   'title' : self.title}
        return render(request, self.template, context)


@method_decorator(login_required, name ='dispatch')
class TaskEditionView(View):

    """
    Updates an specific task
    """

    template = "task_edit.html"
    form = TaskForm
    title = "Editar Tarea"

    def dispatch(self, request, *args, **kwargs):
        self.task = get_object_or_404(Task, pk=kwargs['pk'])
        if self.task.user != request.user:
            return HttpResponseForbidden("No tienes permiso para acceder a esta tarea.")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form(instance=self.task, initial={'due_date': self.task.due_date})
        context = {
            'task': self.task,
            'form': form,
            'title': self.title}
        return render(request, self.template, context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST, instance=self.task)
        if form.is_valid():
            task = form.save(commit=False)
            task.user_id = request.user.id
            task.save()
            return redirect('task_item', pk=self.task.pk)
        context = {
            'form': form,
            'title': self.title}
        return render(request, self.template, context)

