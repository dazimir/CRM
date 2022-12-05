from .models import Task, Card
from django.forms import ModelForm, TextInput, Textarea, DateField, DateInput, SelectDateWidget


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task", "idate"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'введите название'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'введите описание'
            }),
            "idate": DateInput(format=('%d-%m-%Y'),
                               attrs={'class': 'form-control-sm datepicker', 'placeholder': 'Select a date',
                                      'type': 'date'})}


# -----------------------------------------------------------------------------------------------------------------------------
# создаем класс КАРТОЧКА ЗАЯВИТЕЛЯ


class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ['last_name', 'name_name', 'first_name', 'place_of_issue', 'division_code', 'date_of_issue',
                  'date_of_birth', 'place_of_birth', 'registration_address', 'residential_address', 'sn_passport',
                  'snils']
        widgets = {
            "last_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилие'}),

            "name_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'}),

            "first_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отчество'}),

            "place_of_issue": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Место выдачи паспорта'}),

            "division_code": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Код подразделения'}),

            "date_of_issue": DateInput(format=('%d-%m-%Y'),
                                       attrs={'type': 'date',
                                              'class': 'form-control',
                                              'placeholder': 'Дата выдачи', 'type': 'date'}),

            "date_of_birth": DateInput(format=('%d-%m-%Y'),
                                       attrs={'type': 'date',
                                              'class': 'form-control',
                                              'placeholder': 'Дата рождения', 'type': 'date'}),

            "place_of_birth": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Место рождения'}),

            "registration_address": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес регистрации'}),

            "residential_address": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фактический адрес'}),

            "sn_passport": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Серия и номер паспорта'}),

            "snils": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'СНИЛС'}),

            "card_search": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО карточки заявителя для поиска'}),
        }
