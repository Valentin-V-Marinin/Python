from os import system
from check import *


def screen():
    system('cls')
    print('Телефонная книга')
    print('='*40)


def main_ui(act: int = 5):
    act = input(
        ' \
    1 - добавить новый контакт\n \
    2 - показать все контакты\n \
    3 - выбрать контакт\n \
    0 - завершить работу\n?:')
    return check_ui(act,'main')


def contact_selected(act: int = 5):
    act = int(input(
        ' \
    1 - удалить контакт\n \
    0 - вернуться в основное меню\n?:'))
    if not act:
        screen()
    return check_ui(act,'aux')
