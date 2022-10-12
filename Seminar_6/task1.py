# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, 
#  значения которых больше предыдущего элемента. Use comprehension.

from random import sample
from itertools import islice

number = int(input('Введите число элементов: '))

def edit_list(numb: int):
    basis = [i for i in sample(range(0,50),k=numb)]
    print(basis)
    return [x for x, y in zip( (islice(basis,1,None)), (islice(basis,0,len(basis)-1)) ) if x > y ]

def edit_list_1(numb: int):
    basis = [i for i in sample(range(0,50),k=numb)]
    print(basis)
    return [x for x, y in zip( basis[1:len(basis)], basis[0:len(basis)-1] ) if x > y ]

def edit_list_2(numb: int):
    basis = [i for i in sample(range(0,50),k=numb)]
    result = []
    count = len(basis)
    i = 0
    while count-i:
        if not i: 
            p = basis[i]
        else:
            if basis[i]>p: 
                result.append(basis[i])
            p = basis[i]
        i+=1
    print(basis)
    return result

print(edit_list(number))
print(edit_list_1(number))
print(edit_list_2(number))
