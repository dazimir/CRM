from django.shortcuts import render, redirect
from .models import Task


def admin(request):
    return render(request, 'admin.html')


def index(request):
    return render(request, 'main/index.html')


def input_task(request):
    return render(request, 'main/input_task.html')


def report_task(request):
    return render(request, 'main/report_task.html')


def status_task(request):
    tasks = Task.objects.all()
    return render(request, 'main/status_task.html', {'title': 'Отчет', 'tasks': tasks })
