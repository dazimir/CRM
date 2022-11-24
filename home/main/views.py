from django.shortcuts import render, redirect
from django import forms
from .models import *
from .forms import TaskForm, Customer_cardForm


def admin(request):
    return render(request, 'admin.html')


def index(request):
    return render(request, 'main/index.html')


def input_task(request):
    error = ''
    if request.method == 'POST':
        form = Customer_cardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Поля заполнены не верно'

    form = Customer_cardForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/input_task.html', context)


def report_task(request):
    return render(request, 'main/report_task.html')


def status_task(request):
    tasks = Task.objects.order_by('-id')
    cards = Сustomer_card.objects.order_by('-id')
    # render(request, 'main/status_task.html', {'title': 'Отчет', 'tasks': tasks}),
    return render(request, 'main/status_task.html', {'title2': 'Карточка', 'cards': cards, 'title1': 'Отчет', 'tasks': tasks})
