from django.contrib import admin
from .models import Label, Task, TaskObservation


admin.site.register(Label)
admin.site.register(Task)
admin.site.register(TaskObservation)