# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

number = int(input('Введите число элемнтов (от нуля): '))

def Fibonacci(num: int):
    basis = []
    for i in range(num+1):
        if (i == 0):
            basis.append(i)
        elif (i == 1):
            basis.insert(0,i)
            basis.append(i) 
        else:    
            basis.insert(0, basis[1] - basis[0])
            basis.append(basis[len(basis)-2] + basis[len(basis)-1])
    return basis

print(Fibonacci(number))