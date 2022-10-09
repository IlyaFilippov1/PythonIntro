# Задайте список из нескольких чисел. Напишите 
# программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях 
# элементы 3 и 9, ответ: 12

""" from random import randrange
n = int(input())
a = [randrange(1,10) for i in range(n)]
print(a)
summa = 0
for i in range(len(a)):
    if i % 2 > 0:
        summa += a[i]
print(summa) """

#Напишите программу, которая найдёт произведение 
#пар чисел списка. Парой считаем первый и последний элемент, 
#второй и предпоследний и т.д.
#Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

""" from random import randrange
n = int(input())
a = [randrange(1,10) for i in range(n)]
print(a)
res = []
v = 1
if n % 2 == 0:
    for i in range(0, int(len(a)//2)):
        res.append(a[i] * a[i-v])
        v += 2
    print(res)
else:
    for i in range(0, int(len(a)//2)):
        res.append(a[i] * a[i-v])
        v += 2
    res.append(a[len(a)//2]**2)
    print(res) """

#Задайте список из вещественных чисел. Напишите программу, которая 
# найдёт разницу между максимальным и минимальным
#  значением дробной части элементов.
#Пример:
#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

""" from random import random, randrange
n = int(input())
array = [randrange(1, 10) + round(float(random()), 2) for i in range(n)]
print(array)

for i in range(len(array)):
    array[i] = round(array[i] - int(array[i]), 2)
print(max(array) - min(array))
 """

#Напишите программу, которая будет 
# преобразовывать десятичное число в двоичное.
#Пример:
#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10

""" from audioop import reverse

dec = int(input('Введите число: '))
n = []

while dec >= 1:
    n.append(dec % 2)
    dec = dec // 2
n.reverse
print("".join(map(str, n))) """

# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.(Доп)
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, -1, 2, -3, 5, -8, 13, -21]

from audioop import reverse

n = 8
fib = [0 for i in range(n+1)]
fib[1] = 1
fib2 = [0 for i in range(n+1)]
fib2[1] = 1
for i in range(2, len(fib)):
    fib[i] = fib[i-1] + fib[i-2]
for i in range(2, len(fib2)):
    fib2[i] = fib2[i-2] - fib2[i-1]
fib2.pop(0)

fib2[::-1] = fib2[0:n]
res = fib2 + fib
print(res)
