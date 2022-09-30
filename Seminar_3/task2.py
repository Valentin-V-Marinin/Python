# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import sample

basic_list = sample(range(-20,20), int(input('Введите количество элементов списка: ')))
print(basic_list)


def Multiplication(my_list: list):
    i = 0
    result_list = []
    while (i < len(my_list)/2):
        if not (len(my_list)-1-2*i):
            result_list.append(my_list[i])
        else:
            result_list.append(my_list[i]*my_list[-i-1])
        i += 1
    return result_list


print(Multiplication(basic_list))
