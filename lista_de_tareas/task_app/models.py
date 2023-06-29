from django.db import models
from django.contrib.auth.models import User




class Label(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title
    

class Task(models.Model):
    STATUS_CHOICE = [
          ('pendiente', 'Pendiente'),
          ('en progreso', 'En progreso'),
          ('completada', 'Completada')
    ]
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    description = models.TextField()
    due_date = models.DateField(blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICE)
    label_id = models.ForeignKey(Label, verbose_name=("etiqueta"), on_delete=models.PROTECT)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def formatted_due_date(self):
            return self.due_date.strftime("%d-%m-%Y %H:%M:%S")
    
    def __str__(self):
        return self.title
    
