from curses.ascii import isdigit


def check_ui(sign, func):
    if str(sign).isdigit():
        if (func == 'main'):
            if 0 <= int(sign) < 4:
                return int(sign)
        if (func == 'aux'):
            if 0 <= int(sign) < 2:
                return int(sign)
    else:
        return 100
    
def err_msg(act):
    if act == 100: print('Некорректный выбор!')
    if act == 101: print('Пустой список!')
    if act == 102: print('Ошибка! Имя/Фамилия содержат цифры.')
    if act == 103: print('Ошибка! Длина Имя/Фамилия/Телефон не соответствует требованииям.')
    
    
def is_empty_list(phone_list: list):
    result = True
    if (len(phone_list) and (phone_list[0] != '\n') and (phone_list[0] != [''])):
        for i in range(len(phone_list)):
            if phone_list[i][4] == 'status1':
                result = False
    return result


def check_name(name: str):
    result = True
    if len(list(filter(lambda x: x.isdigit(), name))):
        result = False
    return result

def check_length(family_contact,name_contact,phone_number):
    result = True
    if 2 <= family_contact <= 20: result = False
    if 2 <= name_contact <= 15: result = False
    if 3 <= phone_number <= 11: result = False
    return result