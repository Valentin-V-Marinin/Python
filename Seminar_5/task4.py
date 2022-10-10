# 4. ** Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход 
# друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать 
# не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# Добавьте игру против бота
# Подумайте как наделить бота "интеллектом"

from random import randint
from secrets import choice

sum = 109
candy_min = 1
candy_max = 28
last_comp_step = 0
last_human_step = 0

def table_draw(pl_1, pl_2, msg: int, pl: list):
    txt = ""
    if msg == 1: txt = "По жребию игрок computer делает первый ход"
    if msg == 2: txt = "По жребию игрок human делает первый ход"
    if msg == 3: txt = "computer - победитель и забирает все конфеты"
    if msg == 4: txt = "human - победитель и забирает все конфеты"
    if msg == 5: txt = "player_1 - победитель и забирает все конфеты"
    if msg == 6: txt = "player_2 - победитель и забирает все конфеты"
    
    print(); print(); print(); print(); print(); print(); print()
    print(f'{txt}')
    if (msg in (3,4,5,6)): print(); print()
    print('За один ход можно взять от 1 до 28 конфет                             "0" - выход из игры')
    print(f'Всего конфет: {sum}      Осталось конфет: {(sum-pl_1-pl_2)}')
    print(f'Конфет у первого игрока ({pl[0]}):{pl_1}')
    print(f'Конфет у второго игрока ({pl[1]}):{pl_2}')
    print(); print(); print()
    

def candies_counter_simple():
    pl = ['player_1','player_2']
    pl_1 = 0; pl_2 = 0; i = 0; msg = 0
    table_draw(pl_1, pl_2, msg, pl)
    
    while (sum-pl_1-pl_2):
        candies = int(input(f'Игрок {pl[i]}, сколько конфет возьмёте?: '))
        if not candies: break
        if not candy_min <= candies <= candy_max: continue
        if candies > (sum-pl_1-pl_2): continue
        
        if i:   pl_2+= candies
        else:   pl_1+= candies

        if not (sum-pl_1-pl_2):
            if i: table_draw(pl_1, pl_2, 6, pl)
            else: table_draw(pl_1, pl_2, 5, pl)
        else:
            table_draw(pl_1, pl_2, msg, pl)
        i = not i


def candies_comp(summa, pl_1, pl_2):
    if pl_1 == 0:
        result = sum - (sum//(candy_min + candy_max))*(candy_min + candy_max)   
    elif (sum-pl_1-pl_2) < (candy_min + candy_max):
        result = sum-pl_1-pl_2
    else:
        result = candy_min + candy_max - summa
    return result

def candies_counter_complicated_comp():
    try:
        pl = ['computer','human']
        pl_1 = 0; pl_2 = 0; comp = 0; msg = 1
        table_draw(pl_1, pl_2, msg, pl)
        
        while (sum-pl_1-pl_2):
            if (sum == (sum-pl_1-pl_2)):
                candies = candies_comp(0, pl_1, pl_2)
                pl_1+= candies
                table_draw(pl_1, pl_2, msg, pl)
            
            if not comp:    
                candies = int(input('Игрок human, сколько конфет возьмёте?: '))
                if not candies: break
                if not candy_min <= candies <= candy_max: continue
                if candies > (sum-pl_1-pl_2): continue
            
            if comp:
                pl_1+= candies_comp(candies, pl_1, pl_2)
            else:
                pl_2+= candies

            if not (sum-pl_1-pl_2):
                if comp: table_draw(pl_1, pl_2, 3, pl)
                else:    table_draw(pl_1, pl_2, 4, pl)
            else:
                table_draw(pl_1, pl_2, msg, pl)
            comp = not comp
    except:
        print('Для ввода доступны только цифры. Начните игру заново.')


def check_human_step(pl_1, pl_2: int):
    if ((sum-pl_1-pl_2) % (candy_min + candy_max) == 0):
        return 1
    else: 
        return 0    
    
def candies_human(candies, pl_1, pl_2):
    return (sum-pl_1-pl_2) % (candy_min + candy_max)
     
def candies_counter_complicated_human():
    try:
        pl = ['human','computer']
        pl_1 = 0; pl_2 = 0; human = 1; msg = 2; flag = 1; interception = 1
        table_draw(pl_1, pl_2, msg, pl)
        
        while (sum-pl_1-pl_2):    
            if human:    
                candies = int(input('Игрок human, сколько конфет возьмёте?: '))
                if not candies: break
                if not candy_min <= candies <= candy_max: continue
                if candies > (sum-pl_1-pl_2): continue
                if not pl_1: flag = check_human_step(candies, 0)
                
            if human:
                pl_1+= candies
                if flag: flag = check_human_step(pl_1, pl_2)
            else:
                if flag:
                    pl_2+= randint(1,28)
                else:
                    if interception:
                        pl_2+= candies_human(candies, pl_1, pl_2)
                        interception = 0
                    else:
                        pl_2+= candies_comp(candies, pl_1, pl_2)
                        
            if not (sum-pl_1-pl_2):
                if human: table_draw(pl_1, pl_2, 4, pl)
                else:     table_draw(pl_1, pl_2, 3, pl)
            else:
                table_draw(pl_1, pl_2, msg, pl)
            human = not human
    except:
        print('Для ввода доступны только цифры. Начните игру заново.')

def play():
    opt = int(input('Играть будете против человека(1) или против компьютера(2)?:'))-1
    if not opt:
        candies_counter_simple()
    else: 
        opt = int(choice('01'))
        if opt: 
            candies_counter_complicated_comp()
        else:
            candies_counter_complicated_human()
    

play()