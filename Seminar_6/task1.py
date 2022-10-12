# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, 
#  значения которых больше предыдущего элемента. Use comprehension.

from random import sample
from itertools import islice

def edit_list():
    basis = [i for i in sample(range(0,50),k=12)]
    print(basis)
    return [x for x, y in zip( (islice(basis,1,None)), (islice(basis,0,len(basis)-1)) ) if x > y ]

def edit_list_1():
    basis = [i for i in sample(range(0,50),k=12)]
    print(basis)
    return [x for x, y in zip( basis[1:len(basis)], basis[0:len(basis)-1] ) if x > y ]

def edit_list_2():
    basis = [i for i in sample(range(0,50),k=12)]
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

print(edit_list())
print(edit_list_1())
print(edit_list_2())
