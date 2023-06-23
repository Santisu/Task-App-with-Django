from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.LoginView.as_view(), name="login" ),
    path('logout/', views.LogoutView, name="logout"),
    path('index_user/', views.IndexUserView.as_view(), name="index_user")

]