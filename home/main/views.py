from django.shortcuts import render, redirect
from django import forms
from .models import *
from .forms import TaskForm, CardForm, TaskobjForm

from .models import Card, Taskobj
from django.shortcuts import render
from .filters import UserFilter

from django.views.generic import DetailView, UpdateView, DeleteView

import datetime


def admin(request):
    return render(request, '/admin')


def index(request):
    return render(request, 'main/index.html')


def input_task(request):
    error = ''
    temp = 'Новая карточка'
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.date_input_card = datetime.date.today()
            obj.save()
            return redirect('/')
        else:
            error = 'Поля заполнены не верно'
    form = CardForm()
    context = {
        'form': form,
        'error': error,
        'temp': temp
    }
    return render(request, 'main/input_task.html', context)


def report_task(request):
    return render(request, 'main/report_task.html')


def input_new_task(request):
    return render(request, 'main/input_new_task.html')


def status_task(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/status_task.html', {'title': 'Отчет', 'tasks': tasks})


def customer_card(request):
    if request.method == 'GET':
        cards = Card.objects.order_by('-id')
        print('------ это GET  -------')
        return render(request, 'main/customer_card.html',
                      {'title2': 'Карточка', 'cards': cards})  # выводим все карточки

    # если нажали кнопку найти по фамилии то проверяем что ввели
    if request.method == 'POST':
        print('------ это POST -------')
        form = UserFilter(request.POST)

        if form.is_valid():
            # print('------ это POST после проверки на валидацию -------')
            cards = Card.objects.all()
            last_name = request.POST.get('last_name')
            user_filter = Card.objects.filter(last_name=last_name)
            print('last_name ------------  ', last_name)

            if last_name != '':
                return render(request, 'main/customer_card.html',
                              {'title2': 'Карточка', 'cards': user_filter})  # если в поле что-то введено то ищем
            else:
                return render(request, 'main/customer_card.html',
                              {'title2': 'Карточка', 'cards': cards})  # если поле input пустое то выводим все карточки


class CardsDeleteView(DeleteView):
    model = Card
    success_url = '/'
    context_object_name = 'article'
    template_name = 'main/card-delete.html'


class CardsUpdateView(UpdateView):
    model = Card
    success_url = '/'
    template_name = 'main/input_task.html'
    context_object_name = 'article'
    form_class = CardForm


# --------------------------------------------------------------------------------------------------------------------

def input_new_task(request):
    error = ''
    form = TaskobjForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/input_new_task.html', context)
