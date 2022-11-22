from django.shortcuts import render, redirect
from django import forms
from .models import *
from .forms import TaskForm


def admin(request):
    return render(request, 'admin.html')


def index(request):
    return render(request, 'main/index.html')


def input_task(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Поля заполнены не верно'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/input_task.html', context)


def report_task(request):
    return render(request, 'main/report_task.html')


def status_task(request):
    tasks = Task.objects.all()
    return render(request, 'main/status_task.html', {'title': 'Отчет', 'tasks': tasks })
