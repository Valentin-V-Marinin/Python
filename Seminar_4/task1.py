# Вычислить число c заданной точностью d

number = float(input('Введите число: '))

def set_accuracy(num):
    accuracy = int(input('Введите количество знаков после запятой (точность): '))
    print(format(num, f'0.{accuracy}f'))
    return (format(num, f'0.{accuracy}f'))

set_accuracy(number)
