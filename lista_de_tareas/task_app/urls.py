from django.urls import path
from .views import TaskListView, TaskItemView, TaskCreationView


urlpatterns = [
    path('tasks_list', TaskListView.as_view(), name="tasks_list"),
    path('task/<int:pk>/', TaskItemView.as_view(), name="task_item"),
    path('task_creation/', TaskCreationView.as_view(), name="task_creation"),
    # path('task_edit/<int:pk>/', TaskEditionView.as_view(), name="task_edition"),
]
