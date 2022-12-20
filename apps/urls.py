from . import views
from django.contrib import admin
from django.urls import path, re_path
from apps.views import *
from apps.models import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.index, name= "index"),
    path('about/', views.about, name="about"),
    path('hello/<str:username>', views.hello, name="hello"),
    path('projects/', views.projects, name="projects"),
    path('projects/<int:id>', views.project_detail, name="project_detail"),
    path('tasks/', views.tasks, name="tasks"),
    path('create_task/', views.create_task, name="create_task"),
    path('create_project/', views.create_project, name="create_project"),
    path('accounts/login/', Login.as_view(), name= 'login'),
    path('logout/', login_required(logoutUsuario), name='logout'),
    path('registro/', RegistroUsuario.as_view(), name='registro'),       
]