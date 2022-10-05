# Вычислить число c заданной точностью d

from decimal import Decimal

number = Decimal(input('Введите число: '))
accuracy = int(input('Введите количество знаков после запятой (точность): '))


def set_accuracy(num, accuracy):
    print(format(num, f'0.{accuracy}f'))
    return (format(num, f'0.{accuracy}f'))

def alter_accuracy(num: Decimal, accuracy):
    print(num.quantize(Decimal(f"0.{10**(accuracy-1)}")))
    return num.quantize(Decimal(f"0.{10**(accuracy-1)}"))

set_accuracy(number, accuracy)
alter_accuracy(number, accuracy)