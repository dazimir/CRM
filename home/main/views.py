from django.shortcuts import render, redirect
from django import forms
from .models import *
from .forms import Task, Card


def admin(request):
    return render(request, '/admin')


def index(request):
    return render(request, 'main/index.html')


def input_task(request):
    error = ''
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Поля заполнены не верно'

    form = CardForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/input_task.html', context)


def report_task(request):
    return render(request, 'main/report_task.html')


def status_task(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/status_task.html', {'title': 'Отчет', 'tasks': tasks})


def customer_card(request):
    cards = Card.objects.order_by('-id')
    return render(request, 'main/customer_card.html', {'title2': 'Карточка', 'cards': cards})
