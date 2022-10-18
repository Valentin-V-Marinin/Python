from itertools import count
from phone_book import *
from check import *
contact = []

def add_new_contact():
    permission = True
    result_code = 10 
    print('Добавление нового контакта в телефонный справочник')
    family_contact = input('Введите фамилию контакта (2-20 символов):')
    name_contact = input('Введите имя контакта (2-15 символов):')
    phone_number = input('Введите телефон контакта (3 - 11 символов):')
    description = input('Введите описание:')
    if not check_name(family_contact+name_contact):
        permission = False
        result_code = 102
    if permission:
        if not check_length(family_contact,name_contact,phone_number):
            permission = False
            result_code = 103
    if permission:
        new_contact = family_contact+";"+name_contact + \
            ";"+str(phone_number)+";"+description+";"+"status1"
        write_data(new_contact)
    return result_code

def show_all_contacts():
    ph_l = []
    data = read_data(1)
    for i in range(len(data)):
            ph_l.append((str(data[i]).replace('\n','')).split(';'))
    if not is_empty_list(ph_l):
        for i in range(len(ph_l)):
            if (ph_l[i][4] == 'status1'):
                print(f'{ph_l[i][0]:15} {ph_l[i][1]:10} {ph_l[i][2]:14} {ph_l[i][3]:12}', end='\n')
        print()
        return 10
    else: return 101


def select_contact():
    global contact
    contact_m = []
    contact = read_data(0, input('Введите имя/фамилию/телефон контакта: '))
    for i in range(len(contact)):
        contact_m.append((str(contact[i]).replace('\n','')).split(';'))
    if not is_empty_list(contact_m):
        for i in range(len(contact_m)):
            if (contact_m[i][4] == 'status1'):
                print(f'{contact_m[i][0]:15} {contact_m[i][1]:10} {contact_m[i][2]:14} {contact_m[i][3]:12} {contact_m[i][4]:15}', \
                end='\n')
        print()
        return 10
    else: return 101
    
    
def delete_contact():
    delete_data(contact)
    contact.clear()
    
