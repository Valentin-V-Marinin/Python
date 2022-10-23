from datetime import *


def check_number(act, pos=0):
    if len(act):
        if not len(list(filter(lambda x: not x.isdigit(), act))):
            if pos < 0: return 10
            if pos:
                if 0 <= int(act) < int(pos):
                    return int(act)
                else:
                    return 100
            else:    
                if 0 <= int(act) < 8:
                    return int(act)
                else:
                    return 100
        else:
            return 100
    else:
        return 100
    
        
def err_msg(act):
    if act == 100: print('Некорректный выбор!')
    if act == 101: print('Пустой список!')
    if act == 102: print('Ошибка! Имя/Фамилия содержат цифры.')
    if act == 103: print('Ошибка! Введённые данные не соответствуют требованиям по длине.')
    if act == 104: print('Ошибка! Нет введённых данных.')
    if act == 105: print('Ошибка! Некорректная дата.')
    if act == 106: print('Ошибка! Некорректное число.')
    
    
def is_empty_list(phone_list: list):
    result = True
    if (len(phone_list) and (phone_list[0] != '\n') and (phone_list[0] != [''])):
        for i in range(len(phone_list)):
            if phone_list[i][4] == 'status1':
                result = False
    return result


def check_name(name: str):
    result = 10
    if len(list(filter(lambda x: x.isdigit(), name))):
        result = 102
    return result

def check_length(pos, data):
    result = 103
    if pos == 1:
        if 2 <= len(data) <= 20: result = 10
    if pos == 2:
        if 2 <= len(data) <= 15: result = 10
    if pos == 3:
        if 5 <= len(data) <= 25: result = 10
    return result


def check_date(birthday):
    try:
        y, m, d = birthday
        birthday = date(int(y), int(m), int(d))
        return (10, birthday)
    except:
        return (105, '00/00/0000')
    
    
def check_float(salary):
    act = 10
    if (',' in salary): salary = salary.replace(',','.')
    if (len(list(filter(lambda x: not x.isdigit(), salary))) == 1) and ('.' not in salary): 
        act = 106
        return act, salary
    if (len(list(filter(lambda x: not x.isdigit(), salary))) > 1): 
        act = 106
        return act, salary
    else: 
        return act, salary
     