from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    title = "webtest"
    return render(request, 'index.html', {
        'titulo': title
    })


def about(request):
    username = 'zeus'
    return render(request, 'about.html', {
        'username': username
    })


def hello(request, username):
    return HttpResponse('<h1>Hello %s</h1>' % username)


def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': projects
    })


def tasks(request):
    # task = Task.objects.get(tittle=tittle)
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })


def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            'form': createnewtask()
        })
    else:
        Task.objects.create(
            tittle=request.POST['title'], description=request.POST['description'], project_id=1)
    return redirect('projects')


def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            "form": createnewprojects()
        })
    else:
        project = Project.objects.create(name=request.POST["name"])
        return redirect('projects')

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html', {
        'project': project,
        'tasks': tasks
    })


# Registrar un usuario

class RegistroUsuario(CreateView):
    model = User
    template_name = 'usuario/registrar.html'
    form_class = ResgistroForm
    success_url = reverse_lazy('login')


# Login 

class Login(FormView):
    template_name = 'usuario/login.html'
    form_class = FormularioLogin

    success_url = reverse_lazy('index')

    @method_decorator(csrf_protect) # Este decorador agrega protección CSRF
    @method_decorator(never_cache)
    def dispatch(self, request, *args , **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else: 
            return super(Login,self).dispatch(request, *args, **kwargs)

    def form_valid(self, form) :
        login(self.request,form.get_user())
        return super(Login, self).form_valid(form)


def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login')