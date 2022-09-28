# Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.

number = int(input('Введите количество элементов списка:'))
sum = 0
result = []

for i in range(1,number+1):
    sum+= round((1+1/i)**i)
    result.append(round((1+1/i)**i))
    
print(f"{result}  {sum}")
