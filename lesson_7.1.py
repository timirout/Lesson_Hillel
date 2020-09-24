# Задача №18 (Задача на множество 2)

"""
Даны два списка чисел. Посчитайте, сколько (уникальных) чисел
содержится одновременно как в первом списке, так и во втором.

  -  Примечание. Эту задачу на Питоне можно решить в одну строчку.
"""
import random

# Вариант решения 1 (Более обширный)
a = set(random.randint(1, 20) for lis1 in range(10))
b = {random.randint(1, 20) for lis2 in range(10)}

print('Первый список:,', a, type(a))
print('Второй список:,', b, type(b))

res = a & b
if not res:
    print('Нет общих элементов!')
else:
    print('Общие элементы певого и второго списка:', res)
    print('Кол-во элемментов содержится одновременно как в первом списке, так и во втором:', len(res))
    print('Тип:', type(res))

# Вариант решения 2 (В одну строку)
print(len(set(random.randint(1, 5) for lis3 in range(10)) & set(random.randint(1, 5) for lis4 in range(10))))

