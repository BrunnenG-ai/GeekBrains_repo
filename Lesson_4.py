print("Задание №1")

from sys import argv


def salary():
    try:
        time, stavka, premia = map(int, argv[1:])
        print(f"Зарплата - {time * stavka + premia}")
    except ValueError:
        print("Введите три числа через пробел, другие значения не допускаются ")


salary()

print("Задание №2")

rnd_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [rnd_list[i] for i in range(1, len(rnd_list)) if rnd_list[i] > rnd_list[i - 1]]

print(new_list)

print("Задание №3")

mult_list = [digit for digit in range(19, 241) if digit % 20 == 0 or digit % 21 == 0]
print(mult_list)

print("Задание №4")

from random import randint

rnd_list = [randint(-10, 10) for i in range(20)]
uniq_list = [el for el in rnd_list if rnd_list.count(el) == 1]
print(f"Исходный список : \n{rnd_list}\nСписок без повторений : \n{uniq_list}")

print("задание №5")

from functools import reduce


def mul_list(digit_1, digit_2):
    return digit_1 * digit_2


uniq_list1 = [dig for dig in range(100, 1001, 2)]
print(f"Уникальный список : \n{uniq_list}\nЭлементы произведения\n{reduce(mul_list, uniq_list)}")

print("Задание №6")

from itertools import count, cycle


def listed():
    for n_6 in count(int(input('Для выхода из программы введите "q", Введите начальное число: '))):
        print(n_6, end='')
        Number = input()
        if Number == 'q':
            break


def repeated():
    list_6 = input('Для выхода из программы введите "q", Для выведения следующего элемента списка нажмите Enter. '
                   'Введите список через пробел: ').split()
    step = cycle(list_6)
    element = None

    while element != 'q':
        print(next(step), end='')
        element = input()


print("Задание №7")

from itertools import count
from math import factorial


def factorial_func():
    for n_7 in count(1):
        yield factorial(n_7)


results_7 = factorial_func()
x = 0
for nu_7 in results_7:
    if x == 15:
        break
    else:
        x += 1
        print(f"Factorial {x} = {nu_7}")
