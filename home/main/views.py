from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django import forms
from django.urls import reverse_lazy

from .models import *
from .forms import CardForm, TaskobjForm, InputFLForm, InputULForm

from .models import Card, Taskobj
from django.shortcuts import render
from .filters import UserFilter, UserCorpFilter

from django.views.generic import DetailView, UpdateView, DeleteView, CreateView

import datetime


def admin(request):
    return render(request, '/admin/')


def index(request):
    return render(request, 'main/index.html')


def login(request):
    return render(request, 'main/login.html')


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        return dict(list(context.items()))


def report_task(request):
    if request.method == 'GET':
        print('------ Ща чё нибудь выведу --------------------')
        tasks = Taskobj.objects.get(pk=3)
        cards = IndividualCustomer.objects.get(pk=1)
        # print('tasks: - ', tasks.values_list)
        # print('cards: - ', cards.values_list)

        context = {'tasks': tasks, 'cards': cards}
        print('--------------------------------')
        # print('tasks = ', tasks['kad_number', 'address'])
        # print('cards = ', cards['last_name'])
        return render(request, 'main/report_task.html', context)


def input_new_task(request):
    return render(request, 'main/input_new_task.html')


def status_task(request):
    return render(request, 'main/status_task.html')


# =======================================================================================================================
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


# =======================================================================================================================
def customer_card_UL(request):
    if request.method == 'GET':
        cards = OrganizationCustomer.objects.order_by('-id')
        print('------ это GET  -------')
        return render(request, 'main/customer_card_UL.html',
                      {'title2': 'Карточка', 'cards': cards})  # выводим все карточки

    # если нажали кнопку найти по фамилии то проверяем что ввели
    if request.method == 'POST':
        print('------ это POST -------')
        form = UserCorpFilter(request.POST)

        if form.is_valid():
            # print('------ это POST после проверки на валидацию -------')
            cards = OrganizationCustomer.objects.all()
            comp_name = request.POST.get('company_name')
            user_filter = OrganizationCustomer.objects.filter(company_name=comp_name)
            print('last_name ------------  ', comp_name)

            if comp_name != '':
                return render(request, 'main/customer_card_UL.html',
                              {'title2': 'Карточка', 'cards': user_filter})  # если в поле что-то введено то ищем
            else:
                return render(request, 'main/customer_card_UL.html',
                              {'title2': 'Карточка', 'cards': cards})  # если поле input пустое то выводим все карточки


# =======================================================================================================================

# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------


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


# =======================================================================================================================


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


# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------

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


# --------------------------------------------------------------------------------------------------------------------
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


# --------------------------------------------------------------------------------------------------------------------
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


# --------------------------------------------------------------------------------------------------------------------
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

# ====================================================================================================================
# ====================================================================================================================
# ====================================================================================================================
