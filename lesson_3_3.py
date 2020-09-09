# Задача №6 (Перевернуть число)

"""
Дано целое, положительное, ТРЁХЗНАЧНОЕ число. Например: 123, 867, 374.
Необходимо его перевернуть. Например, если ввели число 123, то должно
получиться на выходе ЧИСЛО 321. ВАЖНО! Работать только с числами. Строки,
оператор IF и циклы использовать НЕЛЬЗЯ!
"""

# Вариант решения №1

num = int(input("Введите любое трёхзначное число от 101 до 999: "))
if num < 101:
    print('Вы ввели число меньше 101!')
elif num > 999:
    print('Вы ввели число больше 999!')
else:
    a = num % 10 * 100
    b = num % 100 // 10 * 10
    c = num // 100

    print(a + b + c)

# Вариант решения №2

num = int(input('Введите любое трёхзначное число от 101 до 999: '))
if num < 101 or num > 999:
    print('Вы ввели не трёхзначное число!')
else:
    a = num % 10
    b = num % 100 // 10
    c = num // 100

    print('{0}{1}{2}'.format(a, b, c))



