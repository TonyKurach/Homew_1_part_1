
#Задание №1. Ввести три числа: m, n, p. Подсчитать количество отрицательных чисел

import random

k = int(input("Введите размер списка:\n"))             # определяем размер списка
A = []                                                 # инициализируем непосредственно список
B = []
m = random.randint(-100, 100)                          # устанавливаем случайный выбор значения для "M" от -100 до 100
print("Значение числа m:")
print(m)                                               # выводим на консоль значение числа "M"
A.append(m)                                            # добавляем данное значение числа "M" в список "А"
n = random.randint(-100, 100)                          # устанавливаем случайный выбор значения для "N" от -100 до 100
print("Значение числа n:")
print(n)                                               # выводим на консоль значение числа "N"
A.append(n)                                            # добавляем данное значение числа "N" в список "А"
p = random.randint(-100, 100)                          # устанавливаем случайный выбор значения для "P" от -100 до 100
print("Значение числа p:")
print(p)                                               # выводим на консоль значение числа "P"
A.append(p)                                            # добавляем данное значение числа "P" в список "А"
print("Отрицательные значения элементов списка А:")
for i in range(k):
    if A[i] < 0:                                       # проверяем элементы списка на значения < 0
       print(A[i])                                     # если такие значения есть - выводим на консоль
       B.append(A)
f = len(B)
print("Количество отрицательных чисел в спсике А:")
print(f)