import re

import csv

from pprint import pprint

#lastname,firstname,surname,organization,position,phone,email

#https://habr.com/ru/post/349860/

with open("Regexp/phonebook_raw.csv", "r", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    # pprint(contacts_list)

    for contact in contacts_list:

        # for word in contact:
        #     pprint(word)
        fio_pattern = r'^([А-ЯЁа-яё]+)(\s*)(,?)([А-ЯЁа-яё]+)(\s*)(,?)([А-ЯЁа-яё]*)(,?)(,?)(,?)'
        result = re.split(fio_pattern, contact)
        # re.findall(fio_pattern, contact)
    # re.split(fio_pattern, contacts_list)
    # for contact in contacts_list:
    #     fio_pattern = r' ^ ([А - ЯЁа - яё] +)(\s *)(, ?)([А - ЯЁа - яё] +)(\s *)(, ?)([А - ЯЁа - яё] *)(,?)(, ?)(,?)'
    #     re.split(fio_pattern, contact)
        # re.findall()
        # x = re.split(r' +', contact[0])
        # print(x)
        # pattern = contact[0]
        # re.findall()
        # if contact[0] == contact[1] or contact[0] == contact[2]:
        #     print(contact[0])
        # for position in contact:
            # if position == contact[0]:
            #     print(position)
            # print(position)
            # if position[0] == position[1] or position[0] == position[2]:
            #     print(position[0])
        # print(contact)

