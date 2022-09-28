# Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.

from random import randrange

number = int(input('Введите количество элементов списка: '))
basis = []
result = []
index = 0

for i in range(number):
    basis.append(i)
print(basis)    
    
while (number != 0):
    index = randrange(number)
    result.append(basis[index])
    basis.remove(basis[index])
    number-=1
print(result)
