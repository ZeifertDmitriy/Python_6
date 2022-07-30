# Задача: предложить улучшения кода для уже решённых задач. ПЯТЬ ШТУК:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# старое решение

# def sum_number(n):
#     res = 0
#     for i in range(len(n)):
#         if n[i].isdigit() == True:
#             res += int(n[i])
#     print(res)
# n = input('Введите вещественное число: ')
#sum_number(n)

n = input('Введите вещественное число: ')
f = [int(i) for i in n if i.isdigit()]
print(sum(f))
