# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

number = int(input('Введите число: '))
factorial = 1
count = 1
result = []

while (count <= number):
    factorial*=count
    result.append(factorial)
    count+=1

print(result)