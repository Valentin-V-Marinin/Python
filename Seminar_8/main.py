from ui import *
from actions import action

def main():
    act = 10
    while act:
        act = menu(act)
        if 0 < act < 8:
            act = action(act)
            
            
main()