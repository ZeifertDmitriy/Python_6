# Задача: предложить улучшения кода для уже решённых задач. ПЯТЬ ШТУК:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# 5. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

# старое решение

import time
from random import randint

# def gen(kol):
#     strk = ''
#     i = 0
#     while i < kol:
#     #for i in kol - 1:
#         a = str(time.time())
#         strk.append(a[-2])
#         i += 1

# kol = int(input('Введите количество знаков: '))
# print(gen(kol))

k = 1
kol = int(input('Введите количество знаков: '))
f = [str(time.time())[-randint(1, 6)] for i in range(kol)]
print(f)