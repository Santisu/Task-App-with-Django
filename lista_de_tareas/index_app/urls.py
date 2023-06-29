from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('index_user/', views.IndexUserView.as_view(), name="index_user")
]
