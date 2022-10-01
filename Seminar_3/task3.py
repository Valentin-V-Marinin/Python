# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк/

number = int(input('Введите число для преобразования: '))

def ConvertDecToBin(num):
    count = 0
    result = 0
    while (num):
        result += num%2 * (10**count)
        num//=2
        count+=1
    return result

print(ConvertDecToBin(number))

