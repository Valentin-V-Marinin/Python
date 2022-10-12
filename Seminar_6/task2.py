# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
from random import sample

number = int(input('Введите число: '))


def edit_list(number: int):
    basis = [i for i in range(0,number+1)]
    return [i for i in basis if ((basis[i]%20==0 or  basis[i]%21==0) and basis[i]!=0)]

print(edit_list(number))
