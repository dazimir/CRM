from django.shortcuts import render, redirect
from django import forms
from .models import *
from .forms import TaskForm, CardForm, TaskobjForm, InputFLForm, InputULForm, SettingsForm

from .models import Card, Taskobj
from django.shortcuts import render
from .filters import UserFilter

from django.views.generic import DetailView, UpdateView, DeleteView

import datetime


def admin(request):
    return render(request, '/admin')


def index(request):
    return render(request, 'main/index.html')


def login_crm(request):
    return render(request, 'main/login.html')


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

#=======================================================================================================================
def customer_card_FL(request):
    if request.method == 'GET':
        cards = IndividualCustomer.objects.order_by('-id')
        print('------ это GET  -------')
        return render(request, 'main/customer_card_FL.html',
                      {'title2': 'Карточка', 'cards': cards})  # выводим все карточки

    # если нажали кнопку найти по фамилии то проверяем что ввели
    if request.method == 'POST':
        print('------ это POST -------')
        form = UserFilter(request.POST)

        if form.is_valid():
            # print('------ это POST после проверки на валидацию -------')
            cards = IndividualCustomer.objects.all()
            last_name = request.POST.get('last_name')
            user_filter = IndividualCustomer.objects.filter(last_name=last_name)
            print('last_name ------------  ', last_name)

            if last_name != '':
                return render(request, 'main/customer_card_FL.html',
                              {'title2': 'Карточка', 'cards': user_filter})  # если в поле что-то введено то ищем
            else:
                return render(request, 'main/customer_card_FL.html',
                              {'title2': 'Карточка', 'cards': cards})  # если поле input пустое то выводим все карточки


#=======================================================================================================================
def customer_card_UL(request):
    if request.method == 'GET':
        cards = OrganizationCustomer.objects.order_by('-id')
        print('------ это GET  -------')
        return render(request, 'main/customer_card_UL.html',
                      {'title2': 'Карточка', 'cards': cards})  # выводим все карточки

    # если нажали кнопку найти по фамилии то проверяем что ввели
    if request.method == 'POST':
        print('------ это POST -------')
        form = UserFilter(request.POST)

        if form.is_valid():
            # print('------ это POST после проверки на валидацию -------')
            cards = OrganizationCustomer.objects.all()
            last_name = request.POST.get('last_name')
            user_filter = OrganizationCustomer.objects.filter(last_name=last_name)
            print('last_name ------------  ', last_name)

            if last_name != '':
                return render(request, 'main/customer_card_UL.html',
                              {'title2': 'Карточка', 'cards': user_filter})  # если в поле что-то введено то ищем
            else:
                return render(request, 'main/customer_card_UL.html',
                              {'title2': 'Карточка', 'cards': cards})  # если поле input пустое то выводим все карточки
#=======================================================================================================================

#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------


class CardsDeleteView_FL(DeleteView):
    model = IndividualCustomer
    success_url = '/'
    context_object_name = 'article'
    template_name = 'main/card-delete_FL.html'


class CardsUpdateView_FL(UpdateView):
    model = IndividualCustomer
    success_url = '/'
    template_name = 'main/input_FL.html'
    context_object_name = 'article'
    form_class = CardForm
#=======================================================================================================================


class CardsDeleteView_UL(DeleteView):
    model = OrganizationCustomer
    success_url = '/'
    context_object_name = 'article'
    template_name = 'main/card-delete_UL.html'


class CardsUpdateView_UL(UpdateView):
    model = OrganizationCustomer
    success_url = '/'
    template_name = 'main/input_UL.html'
    context_object_name = 'article'
    form_class = InputULForm

#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------

def input_new_task(request):
    error = ''
    if request.method == 'POST':
        form = TaskobjForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Поля заполнены не верно'
    form = TaskobjForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/input_new_task.html', context)

#--------------------------------------------------------------------------------------------------------------------
def input_FL(request):
    error = ''
    if request.method == 'POST':
        form = InputFLForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Поля заполнены не верно'
    form = InputFLForm()
    context = {
        'form': form,
        'error': error,
        'page_title': 'Ввод данных заявителя, физическое лицо',
        'temp': 'НОВАЯ'
    }
    return render(request, 'main/input_FL.html', context)


#--------------------------------------------------------------------------------------------------------------------
def input_UL(request):
    error = ''
    if request.method == 'POST':
        form = InputULForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Поля заполнены не верно'
    form = InputULForm()
    context = {
        'form': form,
        'error': error,
        'page_title': 'Ввод данных заявителя, юридического лица',
        'temp': 'НОВАЯ'
    }
    return render(request, 'main/input_UL.html', context)


#--------------------------------------------------------------------------------------------------------------------
def settings_crm(request):
    error = ''
    if request.method == 'POST':
        form = SettingsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Поля заполнены не верно'
    form = SettingsForm()
    context = {
        'form': form,
        'error': error,
        'page_title': 'Настройка CRM'
    }
    return render(request, 'main/settings_crm.html', context)

#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
