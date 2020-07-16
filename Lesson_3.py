
print("\n Задание №1 \n")


def task_1(a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError:  # При делении на нол выдаем ошибку
        return "Нельзя делить на ноль !"


print(task_1(int(input("Введите делимое = ")), int(input("Введите делитель = "))))

print("\n Задание №2 \n")


def task_2(Last_Name, Name, City, Birth, Cell, Email):
    print(
        f" Имя - {Name}, Фамилия - {Last_Name}, Дата рождения - {Birth}, Город -  {City}, Электронный адрес - {Email}, Сотовый телефон - {Cell}")


task_2(Name=input("Введите имя : "), Last_Name=input("Введите фамилию : "), Birth=input("Введите дату рождения : "),
       City=input("Введите город : "), Email=input("Введите Email : "), Cell=input("Введите телефон : "))

print("\n Задание №3 \n")


def task_3(first, second, third):
    Summa = first + second + third - min(first, second, third)  # считаем сумму и исключаем минимальное.
    print("Сумма равна = ", Summa)


task_3(int(input("Введите первое значение = ")), int(input("Введите второе значение = ")),
       int(input("Введите третье значение = ")))

print("\n Задание №4 \n")


def task_4(var_1, var_2):
    composition_1 = var_1 ** var_2  # Сначала возводим в степень с помощью звездочек.
    print(f"Первый вариант = {composition_1}")
    i = 0
    composition_2 = 1
    while i != abs(var_2):  # Умножаем var_2 количество раз var_1 на него самого.
        composition_2 = composition_2 * var_1
        i += 1
    else:
        print(f"Второй вариант = {1 / composition_2}")


task_4(abs(int(input("Действительное положительное число = "))), int(input("Целое отрицательное число = ")))

print("\n Задание №5 \n")

end = False  # Булева переменная для завершения цикла
Total = 0  # Переменная в которую складываем значение суммы из функции


def counting(frm_list):
    global end  # End должна быть глобальной так как будет свидетельствовать о завершении цикла.
   #Начало цикла перебора каждого элемента для того, чтобы преобразовать в инт каждый элемент и найти Q,
    #для выхода
    Preliminary = 0  # Промежуточная функция которую будем передавать на выход
    for i in range(0, len(frm_list)):

        if frm_list[i] == "Q":
            frm_list.remove("Q")
            end = True
            break
        else:
            frm_list[i] = int(frm_list[i])
            Preliminary = Preliminary + frm_list[i]  # Промежуточная функция пополняется на каждом шаге

    return Preliminary


while end == False:
    my_list = input('Для выхода введите ' + '\033[91m' + 'Q' + '\033[0m' + ' Введите строку цифр : ')
    frm_list = my_list.split()
    Total = Total + counting(frm_list)
    print("Промежуточная сумма : ", Total)

else:
    print(f"Сумма равна = {Total}")

print("\n Задание №6 \n")

Upper_text = ""


def int_func(text):
    if text.islower() == False:
        return False
    else:
        frm_text[i] = text.title()
        return frm_text[i]


text = input("Введите строку с маленькой буквы : ")
frm_text = text.split()
for i in range(0, len(frm_text)):
    Check = int_func(frm_text[i])
    if Check == False:
        print("Строка состоит не только из маленьких букв!")
        break
    else:
        Upper_text = Upper_text + " " + Check
if Check == False:
    pass
else:
    print("Вот ответ :", Upper_text)
