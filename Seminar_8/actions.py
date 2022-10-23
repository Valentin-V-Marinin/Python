from data import *
from ui import *
from itertools import *
import copy

under_line = 108
employee_list = []
employee_list_extended = []
employee_dict = { 
    'surname': [], 'name': [], 'patronymic': [],
    'birthday': [], 'position': [], 'salary': []}
employee_dict_extended = {'id': {}, 
    'surname': [], 'name': [], 'patronymic': [],
    'birthday': [], 'position': [], 'salary': []}


def action(act):
    if act == 1: act = show_all_records()
    if act == 2: act = search_record()
    if act == 3: act = position_select()
    if act == 4: act = salary_select()
    if act == 5: act = add_employee()
    if act == 6: act = edit_employee()
    if act == 7: act = del_employee()
    return act


def stop(under_line=108):
    print('-'*under_line)
    input('Нажмите "Enter" для продолжения')
    

def data_clear():
    global employee_list
    global employee_list_extended
    global employee_dict
    global employee_dict_extended
    employee_list.clear()
    employee_list_extended.clear()
    employee_dict.clear()
    employee_dict_extended.clear()
    


def list_print(i: int):
    global employee_list
    print('{:20} {:15} {:20} {} {:25} {:12.2f}'.format(str(employee_list[i]['surname']), employee_list[i]['name'], \
    employee_list[i]['patronymic'], employee_list[i]['birthday'], \
        employee_list[i]['position'], float(employee_list[i]['salary'])))


def list_print_extended(i: int):
    global employee_list_extended
    print('{:4} {:20} {:15} {:20} {} {:25} {:12.2f}'.format(employee_list_extended[i]['id'], 
    employee_list_extended[i]['surname'], employee_list_extended[i]['name'], 
    employee_list_extended[i]['patronymic'], employee_list_extended[i]['birthday'], 
        employee_list_extended[i]['position'], float(employee_list_extended[i]['salary'])))


def show_all_records():
    global employee_list
    global employee_dict
    if (len(employee_list) == 0):
        read_data(employee_list)
    if (len(employee_list) != 0):
        for i in range(len(employee_list)):
            list_print(i)
        stop()
        return 10
    else:
        return 101


def search_record():
    global employee_list
    global employee_dict
    if (len(employee_list) == 0):
        read_data(employee_list)
    if (len(employee_list) != 0):
        employee_selection_draw()
        pos = input('Введите фамилию или часть фамилии для поиска: ')
        if len(pos):
            employee_selection_draw(pos)
            for i in range(len(employee_list)):
                if pos in employee_list[i]['surname']:
                    list_print(i)        
            stop()
            return 10
    else:
        return 101


def position_select():
    global employee_list
    if (len(employee_list) == 0):
        read_data(employee_list)
    if (len(employee_list) != 0):
        position_selection_draw('',under_line)
        pos_list = sorted(list(i['position'] for i in employee_list))
        pos_list = [k for k, g in groupby(pos_list)]
        pos_list = list(enumerate(pos_list))
        for i in range(len(pos_list)): print(pos_list[i])
        print('-'*under_line)
        number = check_number(input('Введите цифру/число должности: '),len(pos_list))
        if number < 100:
            position_selection_draw(pos_list[number][1])
            for i in range(len(employee_list)):
                if employee_list[i]['position'] == pos_list[number][1]:
                    list_print(i)        
            stop()
            return 10
        else: 
            return number
    else:
        return 101

def salary_select():
    global employee_list
    global employee_dict
    if (len(employee_list) == 0):
        read_data(employee_list)
    if (len(employee_list) != 0):
        salary_selection_draw()
        pos_n = input('Введите нижнюю границу поиска: ')
        act = check_number(pos_n, -1)
        if act < 100:
            pos_v = input('Введите верхнюю границу поиска: ')
            act = check_number(pos_v, -1)
            if act < 100:
                pos_n = int(pos_n); pos_v = int(pos_v) 
                if (pos_n > 0) and (pos_v > 0):
                    salary_selection_draw(pos_n,pos_v)
                    for i in range(len(employee_list)):
                        if float(pos_n) <= float(employee_list[i]['salary']) <= float(pos_v):
                            list_print(i)        
                    stop()
                    return 10
                elif (pos_n == 0) and (pos_v > 0):
                    salary_selection_draw(pos_n,pos_v)
                    for i in range(len(employee_list)):
                        if float(employee_list[i]['salary']) <= float(pos_v):
                            list_print(i)        
                    stop()
                    return 10
                elif (pos_n > 0) and (pos_v == 0):
                    salary_selection_draw(pos_n,pos_v)
                    for i in range(len(employee_list)):
                        if float(employee_list[i]['salary']) >= float(pos_n):
                            list_print(i)        
                    stop()
                    return 10
                else:
                    return 101
            else:
                return act
        else:
            return act
    else:
        return 101


def add_employee():
    pers_card = { 
        'surname': '', 'name': '', 'patronymic': '',
        'birthday': '', 'position': '', 'salary': 0.00}
    return fill_personal_card(pers_card)


def edit_employee():
    global employee_list_extended
    global employee_dict_extended
    global under_line
    under_line = 112
    edit_employee_draw(pos='')
    if (len(employee_list_extended) == 0):
        read_data_extended(employee_list_extended)
    if (len(employee_list_extended) != 0):
        for i in range(len(employee_list_extended)):
            list_print_extended(i)
        print('-'*under_line)
        id_emp = input('Введите номер карточки сотрудника(id) для редактирования: ') 
        act = check_number(id_emp, -1)
        if act < 100:
            s = list(employee_list_extended[i]['id'] for i in range(len(employee_list_extended)))
            j = len(list(filter(lambda x: int(x) == int(id_emp), s))) 
            if not j: act = 100
        if act < 100 and j:
            d_emp = copy.deepcopy(employee_list_extended)
            idx = s.index(id_emp)
            d_emp = d_emp[idx]
            del d_emp['id']
            old_log_line = log_string_shaping(2, d_emp); log_flag = 0
            personal_card_draw(d_emp,under_line)
            print('Если позиция не нуждается в редактировании нажмите "Enter"')            
            print('Для редактируемой позиции вводите новое значение')
            pos = input('Корректировка позиции "Фамилия": ')            
            if pos == '': 
                personal_card_draw(d_emp,under_line)
                act = 10
            else: 
                act = check_name(pos)
                if act == 10: act = check_length(1, pos)
                if act == 10: 
                    d_emp['surname'] = pos
                    personal_card_draw(d_emp,under_line)
                    employee_list_extended[idx]['surname'] = pos
                    log_flag = 1
                else: return act
            if act == 10:                         
                pos = input('Корректировка позиции "Имя": ')            
                if pos == '': 
                    personal_card_draw(d_emp,under_line)
                    act = 10
                else: 
                    act = check_name(pos)
                    if act == 10: act = check_length(2, pos)
                    if act == 10: 
                        d_emp['name'] = pos
                        personal_card_draw(d_emp,under_line)
                        employee_list_extended[idx]['name'] = pos
                        log_flag = 1
            else: return act
            if act == 10:                         
                pos = input('Корректировка позиции "Отчество": ')            
                if pos == '': 
                    personal_card_draw(d_emp,under_line)
                    act = 10
                else: 
                    act = check_name(pos)
                    if act == 10: act = check_length(3, pos)
                    if act == 10: 
                        d_emp['patronymic'] = pos
                        personal_card_draw(d_emp,under_line)
                        employee_list_extended[idx]['patronymic'] = pos
                        log_flag = 1
            else: return act
            if act == 10:                         
                pos = input('Корректировка позиции "Дата рождения" (гггг,м,д): ').split(',')            
                if pos == [''] or pos == '': 
                    personal_card_draw(d_emp,under_line)
                    act = 10
                else: 
                    act, pos = check_date(pos)
                    if act == 10: 
                        d_emp['birthday'] = pos
                        personal_card_draw(d_emp,under_line)
                        employee_list_extended[idx]['birthday'] = pos
                        log_flag = 1
            else: return act
            if act == 10:                         
                pos = input('Корректировка позиции "Должность": ')            
                if pos == '': 
                    personal_card_draw(d_emp,under_line)
                    act = 10
                else: 
                    if act == 10: 
                        d_emp['position'] = pos
                        personal_card_draw(d_emp,under_line)
                        employee_list_extended[idx]['position'] = pos
                        log_flag = 1
            else: return act
            if act == 10:                         
                pos = input('Корректировка позиции "Зарплата": ')            
                if pos == '': 
                    personal_card_draw(d_emp,under_line)
                    act = 10
                else: 
                    act, pos = check_float(pos)
                    if act == 10: 
                        d_emp['salary'] = pos
                        personal_card_draw(d_emp,under_line)
                        employee_list_extended[idx]['salary'] = pos
                        log_flag = 1
            if act == 10:
                write_data_extended(employee_list_extended)
                if log_flag:
                    log_write(old_log_line)
                    log_write(log_string_shaping(2, d_emp))
                data_clear()
            else: return act
            
            return act
        else:
            return act 
    else:
        return 101
    


def del_employee():
    global employee_list_extended
    global under_line
    under_line = 112
    del_employee_draw(under_line)
    if (len(employee_list_extended) == 0):
        read_data_extended(employee_list_extended)
    if (len(employee_list_extended) != 0):
        for i in range(len(employee_list_extended)):
            list_print_extended(i)
        print('-'*under_line)
        id_emp = input('Введите номер карточки сотрудника(id), который будет удалён: ') 
        act = check_number(id_emp, len(employee_list_extended))
        if act < 100:
            id_emp = int(id_emp)
            s = list(employee_list_extended[i]['id'] for i in range(len(employee_list_extended)))
            j = len(list(filter(lambda x: int(x) == id_emp, s)))
            if j:
                idx = s.index(str(id_emp))
                log_write(log_string_shaping(3,employee_list_extended[idx]))
                employee_list_extended.pop(idx)
                write_data_extended(employee_list_extended)
                data_clear()
                act = 10
            else:
                act = 100
        return act
    else:
        return 101


def add_to_list(pers_card):
    global employee_list
    employee_list.append(dict(pers_card))


def fill_personal_card(pers_card):
    global employee_list
    global employee_dict
    if (len(employee_list) == 0):
        read_data(employee_list)
    personal_card_draw(pers_card)
    surname = input('Введите фамилию сотрудника (2-20 символов): ')
    act = check_name(surname)
    if act == 10: act = check_length(1, surname)
    if act == 10: pers_card['surname'] = surname; personal_card_draw(pers_card)

    if act == 10:
        name = input('Введите имя сотрудника (2-15 символов): ')
        act = check_name(name)
        if act == 10: act = check_length(2, name)
        if act == 10: pers_card['name'] = name; personal_card_draw(pers_card)
    if act == 10:
        patronymic = input('Введите отчество сотрудника (2-15 символов): ')
        act = check_name(patronymic)
        if act == 10: act = check_length(2, patronymic)
        if act == 10: pers_card['patronymic'] = patronymic; personal_card_draw(pers_card)
    if act == 10:    
        birthday = input('Введите дату рождения сотрудника (гггг,м,д): ').split(',')
        act, birthday = check_date(birthday)
        if act == 10: pers_card['birthday'] = birthday; personal_card_draw(pers_card)
    if act == 10:    
        position = input('Введите должность сотрудника (5-25 символов): ')
        if act == 10: act = check_length(3, position)
        if act == 10: pers_card['position'] = position; personal_card_draw(pers_card)
    if act == 10:
        salary = input('Введите зарплату сотрудника (рубли.копейки): ')
        if act == 10: act, salary = check_float(salary)
        if act == 10: pers_card['salary'] = salary; personal_card_draw(pers_card)
    if act == 10:
        add_to_list(pers_card)
        write_data(employee_list)
        log_write(log_string_shaping(1,pers_card))
        data_clear()        
        
    return act


def log_string_shaping(param: int, d: dict):
    if param == 1: line = "add ; "
    if param == 2: line = "edit; "
    if param == 3: line = "del ; "
    
    line += datetime.strftime( datetime.today(),"%Y/%m/%d") + "; "
    line += ('{};{};{};{};{};{:.2f}'.format(
        d['surname'], d['name'], d['patronymic'], d['birthday'], \
        d['position'], float(d['salary'])))
    return line