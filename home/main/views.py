from django.shortcuts import render, redirect
from django.http import HttpResponse


def admin(request):
    return render(request, 'admin.html')


def index(request):
    return render(request, 'main/index.html')


def input_task(request):
    return render(request, 'main/input_task.html')


def report_task(request):
    return render(request, 'main/report_task.html')


def status_task(request):
    return render(request, 'main/status_task.html')
