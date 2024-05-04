class Field:
    def __init__(self, name, reference=None, verbose=''):
        self.name = name
        self.reference = reference
        self.verbose = verbose


class Model:
    table_name = ''
    view_name = ''
    name = ''
    fields = []
    foreign_field = ''
    view_fields = []


class Users(Model):
    table_name = 'users'
    view_name = 'users'
    name = 'Уч. записи'
    fields = [
        Field('username', verbose='Логин'),
        Field('password', verbose='Пароль'),
        Field('role', verbose='Роль')
    ]
    foreign_field = 'username'


class Service(Model):
    table_name = 'service'
    view_name = 'service'
    name = 'Услуги'
    fields = [
        Field('name', verbose='Название'),
        Field('cost', verbose='Стоимость'),
        Field('description', verbose='Описание')
    ]
    foreign_field = 'name'


class Promotion(Model):
    table_name = 'promotion'
    view_name = 'promotion_view'
    name = 'Акции'
    fields = [
        Field('service_id', reference=Service,
              verbose='Услуга'),
        Field('discount', verbose='Скидка'),
        Field('start_date', verbose='Начало'),
        Field('end_date', verbose='Окончание')
    ]
    view_fields = ['promotion_id', 'service_name', 'discount', 'start_date', 'end_date']


class Client(Model):
    table_name = 'client'
    view_name = 'client_view'
    name = 'Клиенты'
    fields = [
        Field('first_name', verbose='Имя'),
        Field('last_name', verbose='Фамилия'),
        Field('phone_number', verbose='Телефон'),
        Field('address', verbose='Адрес'),
        Field('user_id', reference=Users, verbose='Уч. запись')
    ]
    foreign_field = "concat(first_name, ' ', last_name)"
    view_fields = ['client_id', 'first_name', 'last_name', 'phone_number', 'address', 'user_username']


class Employee(Model):
    table_name = 'employee'
    view_name = 'employee_view'
    name = 'Сотрудники'
    fields = [
        Field('first_name', verbose='Имя'),
        Field('last_name', verbose='Фамилия'),
        Field('salary', verbose='Зарплата'),
        Field('user_id', reference=Users, verbose='Уч. запись')
    ]
    foreign_field = "concat(first_name, ' ', last_name)"
    view_fields = ['employee_id', 'first_name', 'last_name', 'salary', 'user_username']


class Record(Model):
    table_name = 'record'
    view_name = 'record_view'
    name = 'Записи'
    fields = [
        Field('client_id', reference=Client, verbose='Клиент'),
        Field('employee_id', reference=Employee,
              verbose='Сотрудник'),
        Field('service_id', reference=Service,
              verbose='Услуга'),
        Field('date', verbose='Дата'),
        Field('review', verbose='Отзыв'),
        Field('status', verbose='Статус')
    ]
    view_fields = ['record_id', 'client_full_name', 'employee_full_name', 'service_name', 'date', 'review', 'status']


class ServiceEmployee(Model):
    table_name = 'service_employee'
    name = 'Услуга-сотрудник'
    fields = [
        Field('service_id', reference=Service,
              verbose='Услуга'),
        Field('employee_id', reference=Employee,
              verbose='Сотрудник')
    ]
