# Напишите программу, которая принимает на вход координаты двух 
#  точек и находит расстояние между ними в 2D пространстве.

x1 = int(input('Введите координату X первой точки: '))
y1 = int(input('Введите координату Y первой точки: '))
x2 = int(input('Введите координату X второй точки: '))
y2 = int(input('Введите координату Y второй точки: '))

print(f"Расстояние между двумя точками равно: {((x2-x1)**2 + (y2-y1)**2)**0.5:.3f}")