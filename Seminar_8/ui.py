from check import *
from os import system

under_line = 108

def menu(act):
    system('cls')
    print('Фирма "Рога и Копыта"')
    print('-'*under_line)
    if (act >= 100): err_msg(act); print('-'*under_line)
    print('1 - показать все записи')
    print('2 - поиск сотрудника по фамилии')
    print('3 - сделать выборку сотрудников по должности')
    print('4 - сделать выборку сотрудников по зарплате')
    print('5 - добавить нового сотрудника')
    print('6 - обновить данные сотрудника')
    print('7 - удалить сотрудника')
    print('0 - закончить работу')
    print('-'*under_line)
    act = check_number(input('Ваше действие? :  '))
    return act
    

def personal_card_draw(d: dict, under_line=108):
    system('cls')
    print('Фирма "Рога и Копыта"')
    print('персональная карточка сотрудника')
    print('-'*under_line)
    print('Фамилия:         ' + d['surname'])
    print('Имя:             ' + d['name'])
    print('Отчество:        ' + d['patronymic'])
    print(f'Дата рождения:   '+ str(d['birthday']))
    print(f'Должность:       ' + d['position'])
    print(f'Зарплата:        '+ str(d['salary']))
    print('-'*under_line)
        

def position_selection_draw(pos='', under_line = 108):
    system('cls')
    print('Фирма "Рога и Копыта"')
    if pos == '':
        print('поиск сотрудников по позиции')
    else:    
        print(f'список сотрудников по позиции: "{pos}"')
    print('-'*under_line)
    
         
def employee_selection_draw(pos=''):
    system('cls')
    print('Фирма "Рога и Копыта"')
    if pos == '':
        print('поиск сотрудников по фамилии')
    else:    
        print(f'список сотрудников по фамилии: "{pos}"')
    print('-'*under_line)
    
    
def salary_selection_draw(pos_n=0, pos_v=0):
    system('cls')
    print('Фирма "Рога и Копыта"')
    if pos_n == pos_v:
        print('выборка сотрудников по размеру зарплаты')
        print('границы выборки указываются целыми числами')
    else:    
        print(f'список сотрудников c зарплатой от "{pos_n}" до "{pos_v}"')
    print('-'*under_line)
    
    
def edit_employee_draw(pos=''):
    system('cls')
    print('Фирма "Рога и Копыта"')
    if pos == '':
        print('выбор сотрудника для редактирования данных')
    else:    
        print(f'внесение изменений в данные сотрудника: "{pos}"')
    print('-'*under_line)


def del_employee_draw(under_line=108):
    system('cls')
    print('Фирма "Рога и Копыта"')
    print('выбор сотрудника для удаления')
    print('-'*under_line)
    
    