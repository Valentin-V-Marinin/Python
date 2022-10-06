# Задайте последовательность чисел. Напишите программу, которая 
#  выведет список неповторяющихся элементов исходной последовательности 
#  в том же порядке.

from random import randrange

number = int(input('Введите количество элементов списка: '))

def random_list(numb):
    result = []
    if numb >= 0:     
        for i in range(numb): 
            result.append(randrange(0,numb))
    else:
        print('Negative value of the number of numbers!')
    return result    

def result_list(mylist : list):
    result = []
    for i in range(len(mylist)):
        if (mylist.count(mylist[i]) == 1): result.append(mylist[i])
    return result

spisok = random_list(number)
print(spisok)
print(result_list(spisok)) 
 