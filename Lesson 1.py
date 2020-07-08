"""Начало Задание 1 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя
несколько чисел и строк и сохраните в переменные, выведите на экран. """

print("\n Задание №1 \n")
name = input("Tell me your name  ")
age = int(input("tell me your age  "))

print("Your name is", name)
print("Your age is", age)

"""Начало Задание 2 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в 
формате чч:мм:сс. Используйте форматирование строк. """
print("\n Задание №2 \n")
new_seconds = int(input("Введите количество секунд которые необходимо перевести в минуты и часы   "))
Seconds_Minutes = int(new_seconds / 60)  # Количество минут в секундах
Seconds_excess = int(new_seconds % 60)  # Остаток секунд после выделения целых минут
Minutes_excess = int(Seconds_Minutes % 60)  # Остаток минут после выделения целых часов
Hours = int(Seconds_Minutes / 60)  # Количество часов

print(f"{Hours:02d}" + ":" + f"{Minutes_excess:02d}" + ":" + f"{Seconds_excess:02d}")

"""Начало Задание 3 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл 
число 3. Считаем 3 + 33 + 333 = 369. """
print("\n Задание №3 \n")
Number_l3 = str(input("Введите любое число : "))  # Первое число
Number_l3_1 = Number_l3 + Number_l3  # Второе число
Number_l3_2 = Number_l3 + Number_l3 + Number_l3  # Третье число
Sum = int(Number_l3) + int(Number_l3_1) + int(Number_l3_2)
print("Сумма будет равна  ", Sum)

"""Начало Задание 4 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для 
решения используйте цикл while и арифметические операции. """
print("\n Задание №4 \n")
Number_l4 = int(input("Введите любое целое положительное число : "))
Max_Number_l4 = 0  # Число для сравнения
while Number_l4 > 0:  # Начало цикла
    Compare = Number_l4 % 10  # Берем первое число с правого конца для сравнения
    Number_l4 = Number_l4 // 10  # Убираем число взятое для сравнения
    if Compare > Max_Number_l4:  # Сравниваемс с максимальным числом на текущий момент 
        Max_Number_l4 = Compare  # Присваиваем максимальное число переменной Max_Number_l4
print("Самое большое число", Max_Number_l4)

"""
Начало Задание 5
5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма 
(прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. 
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). 
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""
print("\n Задание №5 \n")
revenue = float(input("Какова прибыль в рублях ?:  "))
charge = float(input("Каковы издержки в рублях ?:  "))
profit = float(revenue - charge)
if profit > 0:
    print(" Финансовый показатель положительный прибыл составила  =  " + f"{profit}" + "  ₽")
    print("Рентабельность составила  =  " + f"{profit / revenue:.2f}")
    Numbers_of_employees = int(input("Введите количество сотрудников фирмы : "))
    print(
        "Прибыль фирмы в расчете на одного сотрудника составила = " + f"{revenue / Numbers_of_employees:.2f}" + "₽ на человека")
else:
    print("Финансовый показатель отрицательный потери составили  =  " + f"{abs(profit)}" + "  ₽")

"""
Начало Задание 6 
6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. 
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, 
на который результат спортсмена составит не менее b километров. Программа должна принимать значения параметров a и b 
и  выводить одно натуральное число — номер дня. 
"""
print("\n Задание №6 \n")
Result = float(input("Введите текущий результат пробежки в киллометрах : "))
Target = float(input("Введите желаемую дистанцию, которую Вы хотели бы пробегать в киллометрах : "))
Day = 1
print("Результат:")
print(f"1-й день: {Result} км.")
while Result <= Target:
    Change = Result * 0.10  # вычисление изменений за прошедший день
    Result = Change + Result  # добавление изменений за прошедший день к результату
    Day += 1  # Переход на следующий день
    print(f"{Day}-й день: {Result:.2f} км.")
print(f"Ответ: на {Day}-й день спортсмен достиг результата - не менее {Target} км.")
