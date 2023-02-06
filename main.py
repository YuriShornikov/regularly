import re

import csv

from pprint import pprint

#lastname,firstname,surname,organization,position,phone,email

#https://habr.com/ru/post/349860/

with open("Regexp/phonebook_raw.csv", "r", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    # pprint(contacts_list)

    correct_list = []
    for contact in contacts_list:
        fio = ' '.join(contact[:3]).split(' ')
        contact[0:3] = fio[0:3]

        if len(contact[5]) < 25:
            pattern = r'^\+?[7-8]?\s?\(?(\d{3})\)?[-\s]?(\d{3})\-?(\d{2})\-?(\d{2})'
            tel = r'+7(\1)\2-\3-\4'
            result = re.sub(pattern, tel, contact[5])
            contact[5] = result

        else:
            pattern = r'^\+?[7-8]?\s?\(?(\d+)\)?[-\s]?(\d+)\-?(\d+)\-(\d+)?\s?\(?[а-я]+\.?\s?(\d+)\)?'
            tel = r'+7(\1)\2-\3-\4 доб.\5'
            result = re.sub(pattern, tel, contact[5])
            contact[5] = result
        # print(contact[5])
        # print(result)

        correct_list.append(contact)
    print(correct_list)

    with open("phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(correct_list)





