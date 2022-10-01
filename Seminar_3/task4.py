# Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов.

from random import randint, random


def FindDifference():
    number = int(input('Введите количество элементов списка: '))
    basis = []
    maximum = 0
    minimum = 0
    result = 0
    for i in range(number):
        result = round(random(),2) + randint(0,number*3)
        basis.append(result)
        if (i == 0):
            maximum = round(result - int(result),2)
            minimum = round(result - int(result),2)
        else:    
            if ((result - int(result)) > maximum): maximum = round(result - int(result),2)
            if ((result - int(result)) < minimum): minimum = round(result - int(result),2)
    return (f"{basis}\n Max: {maximum}, Min: {minimum}, Difference: {round(abs(maximum-minimum),2)}")

print(FindDifference())

