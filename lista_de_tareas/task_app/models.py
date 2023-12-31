from django.db import models
from django.contrib.auth.models import User

class Label(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=25)
    description = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title
    
class Priority(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=25)
    rank = models.IntegerField()
    description = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title
    
class Task(models.Model):
    STATUS_CHOICE = [
          ('Pendiente', 'Pendiente'),
          ('En Progreso', 'En progreso'),
          ('Completada', 'Completada')
    ]
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    description = models.TextField()
    due_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICE)
    label = models.ForeignKey(Label, verbose_name=("etiqueta"), on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.ForeignKey(Priority, null=True, blank=True, on_delete=models.SET_NULL)

    def formatted_due_date(self):
            return self.due_date.strftime("%d-%m-%Y")
    
    def __str__(self):
        return self.title
    

class TaskObservation(models.Model):
    observation = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return self.observation
    


