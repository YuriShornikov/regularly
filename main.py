import re

import csv

# from pprint import pprint

#lastname,firstname,surname,organization,position,phone,email

#https://habr.com/ru/post/349860/

with open("Regexp/phonebook_raw.csv", "r", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

    correct_list = [] #создаю свой список для записей
    for contact in contacts_list:
        fio = ' '.join(contact[:3]).split(' ')
        contact[0:3] = fio[0:3] #замена первых трех значений строки

        if len(contact[5]) < 25: #проверка длины номера для добавочного номера
            pattern = r'^\+?[7-8]?\s?\(?(\d{3})\)?[-\s]?(\d{3})\-?(\d{2})\-?(\d{2})'
            tel = r'+7(\1)\2-\3-\4'
            result = re.sub(pattern, tel, contact[5])
            contact[5] = result

        else:
            pattern = r'^\+?[7-8]?\s?\(?(\d+)\)?[-\s]?(\d+)\-?(\d+)\-(\d+)?\s?\(?[а-я]+\.?\s?(\d+)\)?'
            tel = r'+7(\1)\2-\3-\4 доб.\5'
            result = re.sub(pattern, tel, contact[5])
            contact[5] = result

        if len(correct_list) == 0: # проверка списка, если элементов нет - записываем
            correct_list.append(contact)
        elif len(correct_list) > 0: #если элементы есть, то даем счетчику 0, и проверяем каждую строку на совпадение первого элемента
            count = 0
            for i in correct_list:
                if contact[0] == i[0]: #если первый элемент совпал, то даем счетчику 1, и начиная с 4 элемента делаем проверку
                    count = 1
                    if len(contact[3]) >= len(i[3]): #если элемент совпадает и больше, то перезаписываем
                        i[3] = contact[3]
                    if len(contact[4]) >= len(i[4]):
                        i[4] = contact[4]
                    if len(contact[5]) >= len(i[5]):
                        i[5] = contact[5]
                    if len(contact[6]) >= len(i[6]):
                        i[6] = contact[6]
            if count != 1: #если совпадений не было найдено, то у счетчика значение 0 и мы записываем строку в список
                correct_list.append(contact)

    print(correct_list)

    with open("phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(correct_list)

    #возможно есть способ красивее и более емкий, хотел бы посмотреть:)



