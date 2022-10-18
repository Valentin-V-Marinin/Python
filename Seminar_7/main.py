from UI import *
from contacts import *
from check import *


def main():
    screen()
    act = 10
    while act:
        act = main_ui()
        if act == 1: 
            screen()
            add_new_contact()
            screen() 
        if act == 2: 
            screen()
            act = show_all_contacts()     
        if act == 3: 
            screen()
            act = select_contact()
            if (act == 10):
                act = contact_selected()
                if act == 1: delete_contact()
                if act == 0: act = 10
                screen()
        if act >= (100):
            screen()
            err_msg(act)

main()