# Напишите программу, которая принимает на вход цифру, 
#  обозначающую день недели, и проверяет, является ли этот день выходным.

weekDay = int(input('Введите номер дня недели: '))
if weekDay in range(1,6):
    print('это будний день')
elif weekDay in (6, 7):
    print('это выходной день')
else:
    print('цифра не корректна') 