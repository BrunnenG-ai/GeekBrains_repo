print("\nTask 1\n")

first_task_lst = ['dog', ('human', 'animal'), [1, 2], 5, 2.4, 0, None, 534, 12, 'dsa']  # Creating list
for x in first_task_lst:  # creating cycle
    print(type(x))

print("\nTask 2 \n")

Second_task_list = []
y = 0
i_task_2 = -1
print("Данная программа записывает введенные вами элементы в список. После чего элемениты обмениваются индексами 0 и 1,"
      " 2 и 3 и.т.д. Если вы хотите завершить ввод элементов просто напишите " + '\033[91m' + 'exit' + '\033[0m')

while y != 'exit':
    y = input("Введите элемент который вы хотели бы добавить : ")
    i_task_2 += 1
    Second_task_list.append(y)
    if y == "exit":
        Second_task_list.remove(y)
        print('Вот получившейся список', Second_task_list)
    if i_task_2 % 2 == 1:
        Second_task_list.insert(i_task_2 - 1, y)
        Second_task_list.pop(-1)

print("\nTask 3 \n")

print('--------------Первый вариант, через list-------------')
while True:
    month = input("Нажмите Q для завершения программы. Введите месяц ввиде целого числа от 1 до 12 : ")
    if month.isdigit() and 0 <= int(month) <= 12:
        month_list = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь",
                      "Ноябрь", "Декабрь"]
        season_list = ["Зима", "Весна", "Лето", "Осень", "Зима"]

        print(f"Вы выбрали {month_list[int(month) - 1]} это {season_list[int(month) // 3]}")
        break
    if month == "Q":
        print("Конец")
        break
    else:
        print("Error!")

print('--------------Второй вариант, через dict-------------')
while True:
    month_2 = input("Нажмите Q для завершения программы. Введите месяц ввиде целого числа от 1 до 12 : ")
    if month_2.isdigit() and 1 <= int(month_2) <= 12:
        month_dict = {1: "Январь", 2: "Февраль", 3: "Март", 4: "Апрель", 5: "Май", 6: "Июнь", 7: "Июль", 8: "Август",
                      9: "Сентябрь", 10: "Октябрь", 11:
                          "Ноябрь", 12: "Декабрь"}
        season_dict = {0: "Зима", 1: "Весна", 2: "Лето", 3: "Осень", 4: "Зима"}

        print(f"Вы выбрали {month_dict[int(month_2)]} это {season_dict[int(month_2) // 3]}")
        break
    if month_2 == "Q":
        print("Конец")
        break
    else:
        print("Error!")

print("\nTask 4 \n")

string = input("Введите строку символов : ")
a = string.split(" ")
for ind, el in enumerate(a):
    if len(el) >= 10:
        print(ind + 1, el[:10])
    else:
        print(ind + 1, el)

print("\nTask 5 \n")

line = [7, 5, 3, 3, 2]
print(line)
digit = int(input("Введите число : "))
n = -1
for i in line:
    n += 1
    if digit > line[n]:
        line.insert(n, float(digit))
        print(line)
        break
    if len(line) == n + 1:
        line.insert(n + 1, float(digit))
        print(line)
        break
