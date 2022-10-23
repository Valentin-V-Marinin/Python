from genericpath import exists
from datetime import *


def read_data(employee_list: list):
    emp = { 
        'surname': [], 'name': [], 'patronymic': [],
        'birthday': [], 'position': [], 'salary': []}
    if exists('persons.csv'):
        with open('persons.csv','r', encoding='utf-8') as p:
            lines = p.readlines()
            for line in lines:
                person = line.strip('\n')
                load_list = person.split(';')
                employee_list.append(dict(surname=load_list[1], \
                    name=load_list[2], patronymic=load_list[3], \
                    birthday=load_list[4], position=load_list[5], \
                    salary=load_list[6]))
        result = 10    
    else: result = 104
    return result


def read_data_extended(employee_list_ext: list):
    emp = {'id': {}, 
        'surname': [], 'name': [], 'patronymic': [],
        'birthday': [], 'position': [], 'salary': []}
    if exists('persons.csv'):
        with open('persons.csv','r', encoding='utf-8') as p:
            lines = p.readlines()
            for line in lines:
                person = line.strip('\n')
                load_list = person.split(';')
                employee_list_ext.append(dict(id=load_list[0], surname=load_list[1], \
                    name=load_list[2], patronymic=load_list[3], \
                    birthday=load_list[4], position=load_list[5], \
                    salary=load_list[6]))
        result = 10    
    else: result = 104
    return result


def write_data(employee_list):
    with open('persons.csv','w', encoding='utf-8') as p:
        for i in range(len(employee_list)):
            line = ('{};{};{};{};{};{};{:.2f}'.format(str(i), \
                str(employee_list[i]['surname']), employee_list[i]['name'], \
                employee_list[i]['patronymic'], employee_list[i]['birthday'], \
                    employee_list[i]['position'], float(employee_list[i]['salary']))) + '\n'
            p.writelines(line)


def write_data_extended(employee_list_ext):
    with open('persons.csv','w', encoding='utf-8') as p:
        for i in range(len(employee_list_ext)):
            line = ('{};{};{};{};{};{};{:.2f}'.format(employee_list_ext[i]['id'], \
                employee_list_ext[i]['surname'], employee_list_ext[i]['name'], \
                employee_list_ext[i]['patronymic'], employee_list_ext[i]['birthday'], \
                    employee_list_ext[i]['position'], float(employee_list_ext[i]['salary']))) + '\n'
            p.writelines(line)


def log_write(line: str):
    with open('log.txt','a', encoding='utf-8') as p:
        p.write(line + '\n')
