import datetime
from django import forms
from .models import Label, Priority, Task, TaskObservation


class TaskFilterForm(forms.Form):
    STATUS_CHOICES = [
        ('all_status', 'Cualquier Estado'),
        ('Pendiente', 'Pendiente'),
        ('En Progreso', 'En Progreso'),
    ]

    max_due = forms.DateField(label='Fecha límite máxima', required=False, widget=forms.DateInput( attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Fecha límite máxima'}))
    

    extra_option = [('all_tasks', 'Todas las etiquetas')]
    labels = Label.objects.all()
    choices = extra_option + [(label.id, label.title) for label in labels]
    
    extra_option_priority = [('all_priority', 'Cualquier prioridad')]
    priority = Priority.objects.all()
    choices_priority = extra_option_priority + [(prior.id, prior.title) for prior in priority]



    label = forms.TypedChoiceField(choices=choices, required=False)
    status = forms.ChoiceField(label='Estado', choices=STATUS_CHOICES, required=False)
    priority = forms.TypedChoiceField(choices=choices_priority, required=False)

class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = 'Título'
        self.fields['description'].label = 'Descripción'
        self.fields['due_date'].label = 'Fecha límite'
        self.fields['status'].label = 'Estado'
        self.fields['label'].label = 'Etiqueta'
        self.fields['user'].label = 'Usuario a asignar'
        self.fields['priority'].label = 'Prioridad'


        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['rows'] = '5'
        self.fields['due_date'].widget.attrs['class'] = 'form-control'
        self.fields['due_date'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['status'].widget.attrs['class'] = 'form-control'
        self.fields['label'].widget.attrs['class'] = 'form-control'
        self.fields['user'].widget.attrs['class'] = 'form-control'
        self.fields['priority'].widget.attrs['class'] = 'form-control'

        instance = kwargs.get('instance')
        if instance and 'due_date' in self.initial:
            due_date = instance.due_date
            if due_date:
                self.initial['due_date'] = due_date.strftime('%Y-%m-%d')
            else: pass
 

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status', 'label', 'priority', 'user']


class ObservationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ObservationForm, self).__init__(*args, **kwargs)
        self.fields['observation'].label = 'Observación'

        self.fields['observation'].widget.attrs['class'] = 'form-control'
        self.fields['observation'].widget.attrs['rows'] = '3'
    class Meta:
        model = TaskObservation
        fields = ['observation']