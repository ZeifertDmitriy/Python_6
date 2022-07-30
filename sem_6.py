# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример

spisok = [1, 2, 3, 5, 1, 5, 3, 10]

# 1
# spisok_v = []
# for i in spisok:
#     if spisok.count(i) == 1:
#         spisok_v.append(i)
# print(spisok_v)

# 2
# lst = [i for i in spisok if spisok.count(i) == 1]

# 3
f = lambda i: spisok.count(i) == 1
lst = list(filter(f, spisok))


print(lst)