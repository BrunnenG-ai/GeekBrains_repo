
print("Задание №1")

with open("l5_1.txt", 'w', encoding='utf-8') as l5_1:
    string_1 = None
    while string_1 != '':
        string_1 = input(f"Введите строку, либо нажмите Enter для выхода : ")
        l5_1.write(f"{string_1}\n")


print("Задание №2")
count = 0
with open("text_3.txt", 'r', encoding='utf-8') as l5_2:
    for i in l5_2:
        count +=1
        list_2 = i.split()
        print(f"Количество слов в {count} строке : {len(list_2)}")
print(f'Общее количество строк {count}')


print("Задание №3")
with open("text_3.txt", 'r', encoding='utf-8') as l5_3:
    count_3 = 0
    Total = 0
    for i in l5_3:
        count_3 += 1
        list_2 = i.split()
        if float(list_2[-1]) < 20000:
            print(f"Зарплата сотрудника {list_2[0]} менее 20к рублей и равна {list_2[-1]}")
            Total += float(list_2[-1])
        else:
            Total += float(list_2[-1])
        
    Average = Total / float(count_3)
    print(f"Средний уровень зарплаты равен {Average}")

print("Задание №4")
rus_list = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("text_4_translated.txt", 'w', encoding='utf-8') as l5_41:
    with open("text_4.txt", 'r', encoding='utf-8') as l5_42:
        for i in l5_42:
            list_3 = i.split()
            l5_41.write(rus_list[list_3[0]] + " - " + list_3[2] + "\n")


print("Задание №5")
string_5 = None
Total = 0
with open("l5_5.txt", 'w', encoding='utf-8') as l5_5:
    while string_5 != '':
        string_5 = input(f"Введите числа разделенные пробелами, либо нажмите Enter для выхода : ")
        l5_5.write(f"{string_5}\n")
with open("l5_5.txt", encoding='utf-8') as l5_51:
    for i in l5_51:
        string_new = map(int, i.split())
        Total += sum(string_new)
print(Total)


print("Задание №6")
dict = {}
with open("text_6.txt", encoding='utf-8') as l5_6:
    for i in l5_6:
        Name, other = i.split(':')
        sort_other = sum(map(int, ''.join([i for i in other if i == ' ' or ('0' <= i <= "9")]).split()))
        dict[Name] = sort_other
    print(f"{dict})")

print("Задание №7")

import json

check = []
with open("text_77.json", "w", encoding='utf-8') as l5_71:
    with open("text_7.txt", encoding='utf-8') as l5_72:
        profit = {}
        for i in l5_72:
            profit[i.split(' ')[0]] = int(i.split(' ')[2]) - int(i.split(' ')[3])
        average_profit = sum([int(i1) for i1 in profit.values() if int(i1) > 0]) / len([int(i1) for i1 in profit.values() if int(i1) > 0])
        check.append(profit)
        check.append({"average_profit": round(average_profit)})
    json.dump(check, l5_71, ensure_ascii=False, indent=4)