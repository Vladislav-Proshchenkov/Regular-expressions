import re
from pprint import pprint

# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ

# Задание 1 Фамилия, Имя, Отчество

count = 0
fio_list = []
for i in contacts_list:
    if contacts_list[count][0] == '':
        contacts_list[count][0] = 'неизвестно'
    if contacts_list[count][1] == '':
        contacts_list[count][1] = 'неизвестно'
    if contacts_list[count][2] == '':
        contacts_list[count][2] = 'неизвестно'
    fio = ' '.join([contacts_list[count][0], contacts_list[count][1], contacts_list[count][2]])
    fio_list.append(fio)
    count += 1
count = 0
for i in contacts_list:
    for m, n in enumerate(fio_list):
        # print(n, m)
        lastname = n.split()[0]
        firstname = n.split()[1]
        surname = n.split()[2]
        # print('фамилия:', lastname, 'имя:', firstname, 'отчество:', surname)
        if m == count:
            i[0] = lastname
            i[1] = firstname
            i[2] = surname
    count += 1
# print(contacts_list)

# Задание 2 Номера телефонов

count = 0
for m, i in enumerate(contacts_list):
    text_phone = contacts_list[m][5]

    pattern = (r"((\+7|8)?\s*\((\d+)\)\s*(\d+)[\s-]*(\d+)[\s-]*(\d+))|"
               r"((\+7)[\s-]*(\d{3})[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2}))|"
               r"((8)[\s-]*(\d{3})[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2}))")
    substr = r"+7(\3\9\15)\4\10\16-\5\11\17-\6\12\18"
    result = re.sub(pattern, substr, text_phone, 0, re.MULTILINE)
    pattern_2 = r"(доб\. (\d{4}))|(\(доб\. (\d{4})\))"
    substr_2 = r"доб.\2\4"
    result_2 = re.sub(pattern_2, substr_2, result, 0, re.MULTILINE)
    # print(result_2)
    if m == count:
        contacts_list[m][5] = result_2
    count += 1

# Задание 3 Объединить все дублирующиеся записи

group_dict = {}

for i in contacts_list:
    key = (i[0], i[1])
    if key not in group_dict:
        group_dict[i[0], i[1]] = i
    else:
        if ((group_dict[i[0], i[1]])[3]) == '':
            group_dict[i[0], i[1]][3] = i[3]
        if ((group_dict[i[0], i[1]])[4]) == '':
            group_dict[i[0], i[1]][4] = i[4]
        if ((group_dict[i[0], i[1]])[5]) == '':
            group_dict[i[0], i[1]][5] = i[5]
        if ((group_dict[i[0], i[1]])[6]) == '':
            group_dict[i[0], i[1]][6] = i[6]

contacts_list = list(group_dict.values())
print(contacts_list)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8", newline="") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)