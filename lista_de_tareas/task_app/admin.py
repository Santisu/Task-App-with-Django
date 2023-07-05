from django.contrib import admin
from .models import Label, Task, TaskObservation, Priority


admin.site.register(Label)
admin.site.register(Task)
admin.site.register(TaskObservation)
admin.site.register(Priority)