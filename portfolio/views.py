from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import Project
from .forms import ProjectForm
# Create your views here.


def home(request):
    projects = Project.objects.all()
    return render(request, "home.html", {"projects": projects})


def signup(request):
    if request.method == "GET":
        return render(request, "signup.html", {
            "form": UserCreationForm
        })
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    username=request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect("home")
            except IntegrityError:
                return render(request, "signup.html", {
                    "form": UserCreationForm, "error": "El usuario ya existe"
                })
        return render(request, "signup.html", {
            "form": UserCreationForm, "error": "Las contraseñas no coinciden"
        })


def signout(request):
    logout(request)
    return redirect("home")


def signin(request):
    if request.method == "GET":
        return render(request, "signin.html", {
            "form": AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST["username"], password=request.POST["password"])
        if user is None:
            return render(request, "signin.html", {
                "form": AuthenticationForm, "error": "El usuario o contraseña no coinciden"
            })
        else:
            login(request, user)
            return redirect("home")


def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, "project_detail.html", {"project": project})


def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProjectForm()
    return render(request, 'create_project.html', {'form': form})


def project_update(request, project_id):
    project = Project.objects.get(pk=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'project_update.html', {'form': form})


def project_delete(request, project_id):
    project = Project.objects.get(pk=project_id)
    if request.method == 'POST':
        project.delete()
        return redirect('home')
    return render(request, 'project_delete.html', {'project': project})
