# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

from decimal import Decimal

number = Decimal(input('Введите число: '))
sum = 0

number*= 10**(len(str(number))-1) 

while(number != 0):
    sum+=number%10
    number//=10
    
print(sum)

