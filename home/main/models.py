from enum import unique
from django.db import models

"""DB login and password"""


class Login(models.Model):
    username = models.CharField('Имя пользователя', max_length=50)
    display_name = models.CharField('Ник', max_length=50)
    password = models.CharField('Пароль', max_length=50)
    email = models.EmailField('Email', max_length=100)
    state = models.CharField('Статус', max_length=10)

    def __str__(self):
        n = str(self.username)
        return n

    def get_absolute_url(self):
        return self.id

    class Meta:
        verbose_name = 'Оператор CRM'
        verbose_name_plural = 'Операторы CRM'


""" DB Республики """


class Republic(models.Model):
    republic = models.CharField('Республика', max_length=50)

    def __str__(self):
        n = str(self.republic)
        return n

    class Meta:
        verbose_name = 'Республика'
        verbose_name_plural = 'Республики'


""" DB Районы """


class Raion(models.Model):
    raion = models.CharField('Район', max_length=50)

    def __str__(self):
        n = str(self.raion)
        return n

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'


""" DB Сельские поселения """


class SelPo(models.Model):
    selpo = models.CharField('Сельское поселение', max_length=70)

    def __str__(self):
        n = str(self.raion)
        return n

    class Meta:
        verbose_name = 'Сельское поселение'
        verbose_name_plural = 'Сельские поселения'


""" DB Населенный пункт """


class Locality(models.Model):
    city = models.CharField('Населенный пункт', max_length=70)

    def __str__(self):
        n = str(self.raion)
        return n

    class Meta:
        verbose_name = 'Населенный пункт'
        verbose_name_plural = 'Населенные пункты'


# =====================================================================================================================
""" DB Заказчик ФЛ """


class IndividualCustomer(models.Model):
    date_input_card = models.DateField('Дата создания карточки', null=True)
    last_name = models.CharField('Фамилия', max_length=50)
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
        verbose_name = 'Заявитель ФЛ'
        verbose_name_plural = 'Заявители ФЛ'


""" DB Заказчик ЮЛ """


class OrganizationCustomer(models.Model):
    date_input_card = models.DateField('Дата')
    company_name = models.CharField('Название фирмы', max_length=200, unique=True)
    inn = models.BigIntegerField('ИНН организации', null=True, blank=True)
    ogrn = models.BigIntegerField('ОГРН организации', null=True, blank=True)
    company_address = models.CharField('Адрес фирмы', max_length=200, unique=True)
    company_phone = models.CharField('Телефон', max_length=50, blank=True, null=True)

    def __str__(self):
        n = str(self.company_name)
        return n

    def get_absolute_url(self):
        return self.id

    class Meta:
        verbose_name = 'Карточка ЮЛ'
        verbose_name_plural = 'Карточки ЮЛ'


# =====================================================================================================================


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
    # one_to_many = models.ForeignKey('IndividualCustomer', on_delete=models.PROTECT)

    date_input_card = models.DateField('Дата создания карточки', null=True)
    name_obj = models.CharField('Название объекта', max_length=150)

    F_U = (('1', 'Физическое лицо'), ('2', 'Юридическое лицо'))
    fl_ul_obj = models.CharField('Физ_Юл', max_length=2, choices=F_U, blank=True)

    job = (
        ('ЗУ', (
            ('01', 'Образование гос.'),
            ('02', 'Раздел гос.'),
            ('03', 'Раздел час.'),
            ('04', 'Перераспределение с гос.'),
            ('05', 'Перераспределение с час.'),
            ('06', 'Уточнение гос.'),
            ('07', 'Уточнение час.'),
            ('08', 'Образование чзу'),
        )),
        ('ОКС', (
            ('11', 'Обрасзование1'),
            ('12', 'Обрасзование2'),
            ('13', 'Обрасзование3'),
            ('14', 'Обрасзование4'),
        )),
        ('Справки', (
            ('21', 'Заключение КИ'),
            ('22', 'Экспертиза'),
            ('23', 'Акт обследования'),
            ('24', 'Сопроводительное'),
        )),
        ('Измерения', (
            ('31', 'Разбивка'),
            ('32', 'Топосъемка'),
            ('33', 'Ортофотосъемка')
        ))
    )
    type_of_work = models.CharField('Вид работы', max_length=2, choices=job, blank=True)
    contract_number = models.CharField('Номер договора', max_length=50)
    date_contract = models.DateField('Дата создания карточки', null=True)

    last_name = models.CharField('Фамилия (ФЛ)', max_length=50, blank=True)
    name_name = models.CharField('Имя (ФЛ)', max_length=50, blank=True)
    first_name = models.CharField('Отчество (ФЛ)', max_length=50, blank=True)

    kad_number = models.CharField('Кадастровый номер', max_length=150, blank=True)
    address = models.CharField('Адрес объекта', blank=True, max_length=250)

    contact_person = models.CharField('Контактное лицо', blank=True, max_length=250)
    contact = models.CharField('Способ контакта', blank=True, max_length=250)
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
