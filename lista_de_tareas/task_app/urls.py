from django.urls import path
from .views import TaskListView, TaskItemView


urlpatterns = [
    path('tasks_list', TaskListView.as_view(), name="tasks_list"),
    path('task/<int:pk>/', TaskItemView.as_view(), name="task_item"),
    
]
