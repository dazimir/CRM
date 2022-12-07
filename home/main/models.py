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

    def get_absolute_url(self):
        return self.id

    class Meta:
        verbose_name = 'Карточка заявителя'
        verbose_name_plural = 'Карточки заявителей'


# =====================================================================================================================

class Taskobj(models.Model):
    date_input_card = models.DateField('Дата создания карточки', null=True)
    name_obj = models.CharField('Название объекта', max_length=150)
    fl_ul_obj = models.BooleanField('ФЛ-ЮЛ')
    # type_of_work = models.TextChoices('Вид работы')
    contract_number = models.CharField('Номер договора', max_length=50)
    date_contract = models.DateField('Дата создания карточки', null=True)

    last_name = models.CharField('Фамилия (ФЛ)', max_length=50, blank=True)
    name_name = models.CharField('Имя (ФЛ)', max_length=50, blank=True)
    first_name = models.CharField('Отчество (ФЛ)', max_length=50, blank=True)

    kad_number = models.CharField('Кадастровый номер', max_length=150, blank=True)
    address = models.CharField('Адрес объекта', blank=True, max_length=250)

    contact_person = models.CharField('Контактное лицо', blank=True, max_length=250)
    contact = models.CharField('Контактная информация', blank=True, max_length=250)
    contact_phone = models.CharField('Контактный телефон', blank=True, max_length=250)
    contact_email = models.EmailField('e-Mail', blank=True, max_length=250)

    information = models.TextField(blank=True)

    def __str__(self):
        n = str(self.name_obj)
        return n

    def get_absolute_url(self):
        return self.id

    class Meta:
        verbose_name = 'Карточка заявки'
        verbose_name_plural = 'Карточки заявок'







# from main.models import Card
# Card.objects.all()
# a = Card.objects.all()[0]


# t = Card.objects.get(last_name='Пипкин')
# t = Card.objects.filter(last_name='Мингазов')
