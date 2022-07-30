# Задача: предложить улучшения кода для уже решённых задач. ПЯТЬ ШТУК:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# 4. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# старое решение

# def Posledov(n):
#     spisok = []
#     sum = 0
#     for i in range(n):
#         spisok.append((1 + 1 / (i + 1)) ** (i + 1))
#         sum += spisok[i]
#         i += 1
#     print(spisok)
#     return sum
# n = input('Введите число: ')
# print(Posledov(int(n)))

n = int(input('Введите число: '))
f = [(1 + 1 / (i + 1)) ** (i + 1) for i in range(n)]
print(sum(f))