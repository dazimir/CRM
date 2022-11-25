from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    idate = models.DateField('дата заявки')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


# Карточка заказчика ФЛ
class Card(models.Model):
    date_input_card = models.DateField('Дата создания карточки', null=True)
    last_name = models.CharField('Фамилие', max_length=50)
    name_name = models.CharField('Имя', max_length=50)
    first_name = models.CharField('Отчество', max_length=50)
    place_of_issue = models.CharField('Место выдачи', max_length=200)
    division_code = models.CharField('Код подразделения', max_length=7)
    date_of_issue = models.DateField('Дата выдачи')
    date_of_birth = models.DateField('Дата рождения')
    place_of_birth = models.CharField('Место рождения', max_length=250)
    registration_address = models.CharField('Адрес регистрации', max_length=250)
    residential_address = models.CharField('Адрес проживания', max_length=250)
    sn_passport = models.CharField('Серия и номер паспорта', max_length=15)
    snils = models.CharField('Номер СНИЛС', max_length=14)

    def __str__(self):
        n = str(self.last_name + ' ' + self.name_name + ' ' + self.first_name)
        return n

    class Meta:
        verbose_name = 'Карточка заявителя'
        verbose_name_plural = 'Карточки заявителей'


# from main.models import Card
# Card.objects.all()
# a = Card.objects.all()[0]
