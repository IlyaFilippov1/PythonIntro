""" Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

Пример:

- 6 -> да
- 7 -> да
- 1 -> нет """

""" n = int(input('день недели: '))
if n == 6 or n == 7:
    print('yes')
else:
    print('no') """

""" Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. """

""" x = int(input('Введите X: '))
y = int(input('Введите Y: '))
z = int(input('Введите Z: '))
if (not (x or y or z)) == (not x and not y and not z):
    print(True)
else:
    print(False) """

""" Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

Пример:

- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3 """

"""x = int(input('Введите X: '))
y = int(input('Введите Y: '))
if x > 0 and y > 0:
    print('1')
elif x < 0 and y > 0:
    print('2')
elif x < 0 and y < 0:
    print('3')
elif x > 0 and y < 0:
    print('4')
elif x == 0 and y == 0:
    print('Начало координат')
elif x == 0 and y != 0:
    print('Точка лежит на оси Y')
elif x != 0 and y == 0:
    print('Точка лежит на оси X') """

""" Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)."""

""" n = int(input("Номер четверти: "))
if n == 1:
    print('x > 0 and y > 0')
elif n == 2:
    print('x < 0 and y > 0')
elif n == 3:
    print('x < 0 and y < 0')
elif n == 4:
    print('x > 0 and y < 0')
else:
    print('error') """

"""Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

Пример:

- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21 """

""" import math

x1 = float(input('введите x1: '))
y1 = float(input('введите y1: '))
x2 = float(input('введите x2: '))
y2 = float(input('введите y2: '))
#res = round(math.sqrt((x2 - x1) **2 + (y2 - y1) **2), 2)
print(f'Расстояние между двумя точками {round(math.sqrt((x2 - x1) **2 + (y2 - y1) **2), 2)}') """

""" Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).

Требуется найти N-е число Фибоначчи.

Входные данные
Во входном файле INPUT.TXT записано целое число N (0 ≤ N ≤ 30).

Выходные данные
В выходной файл OUTPUT.TXT выведите N-е число Фибоначчи. """

""" n = int(input('Введите N от 0 до 30: '))
fib1 = 1
fib2 = 1
fib_sum = 1
for i in range(n - 2):
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
if n > 0:
    print(fib_sum) """