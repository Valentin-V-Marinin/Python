# Создайте программу для игры в "Крестики-нолики". Поле 3x3. Игрок - игрок, без бота.


def table_draw(t: list, msg: int):
    if (msg == 0): txt = "Ход игрока player_2"
    if (msg == 1): txt = "Ход игрока player_1"    
    if (msg == 2): txt = ""    
    if (msg == 3): txt = "Победил   player_1"    
    if (msg == 4): txt = "Победил   player_2"
    if (msg == 5): txt = "Ничья!"
    if (msg == 6): txt = "Игра прервана"
    if (msg == 7): txt = "Некорректный ввод"
        
    print(); print(); print(); print(); print(); print(); print(); print()
    print('                     -------------------')
    print(f'                     |  {t[0]}  |  {t[1]}  |  {t[2]}  |')
    print('                     -------------------                "0" - выйти из игры')
    print(f'                     |  {t[3]}  |  {t[4]}  |  {t[5]}  |')
    print(f'                     -------------------                {txt}')
    print(f'                     |  {t[6]}  |  {t[7]}  |  {t[8]}  |')
    print('                     -------------------')
    print(); print(); print(); print()


def check_game_over(check_set: set,):
    victory_set = [{1,2,3},{4,5,6},{7,8,9},{1,4,7},{2,5,8},{3,6,9},{1,5,9},{3,5,7}]
    result = 0
    for i in range(len(victory_set)):
        if victory_set[i] <= check_set: 
            result = 1
            break
    return result
    

def play():
    try:
        lst = [1,2,3,4,5,6,7,8,9]
        ls  = [1,2,3,4,5,6,7,8,9]    
        table_draw(lst,1)
        pl = ['player_1','player_2']
        pl_1 = set(); pl_2 = set()
        i = 0
        
        while len(ls):
            position = int(input(f'{pl[i]}, Ваш ход, введите цифру позиции: '))
            if (position == 0): 
                table_draw(lst,6)
                break
            if i:
                lst[position-1] = 'X'
                pl_2.add(position)
                if check_game_over(pl_2): 
                    table_draw(lst,4)
                    break
            else:
                lst[position-1] = 'O'
                pl_1.add(position)
                if check_game_over(pl_1): 
                    table_draw(lst,3)
                    break
                
            table_draw(lst,i)
            i = not i
            ls.remove(position)
        
        if not len(ls): table_draw(lst,5)
    except:
        table_draw(lst,7)
        print('Для ввода доступны только цифры. Начните игру заново.')
        
play()
        
    