# Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

from random import sample

basic_list = sample(range(50),int(input('Введите количество элементов списка: ')))
print(basic_list)

def Sum(my_list : list):
    summa = 0
    for i in range(0,len(my_list),2):
        summa+= my_list[i]
    return summa
    
print(Sum(basic_list))