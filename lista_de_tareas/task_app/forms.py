from django import forms
from .models import Label, Task
from django.contrib.auth.models import User


class TaskFilterForm(forms.Form):
    extra_option = [('all', 'Todas las tareas')]
    labels = Label.objects.all()
    choices = extra_option + [(label.id, label.title) for label in labels]
    
    label = forms.TypedChoiceField(choices=choices, required=False)

class TaskCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TaskCreationForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = 'Título'
        self.fields['description'].label = 'Descripción'
        self.fields['due_date'].label = 'Fecha límite'
        self.fields['status'].label = 'Estado'
        self.fields['label'].label = 'Etiqueta'


        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['due_date'].widget.attrs['class'] = 'form-control'
        self.fields['due_date'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})
        self.fields['status'].widget.attrs['class'] = 'form-control'
        self.fields['label'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status', 'label']