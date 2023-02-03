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
        # print(contact[0])
        text = ', '.join(contact)
        # fio_pattern = r'([А-ЯЁа-яё]+)(\s*)(,?)([А-ЯЁа-яё]+)(\s*)(,?)([А-ЯЁа-яё]*)(,?),?)(,?)(,?)'
        pattern = r'^[А-ЯЁа-яё]+\s*,?\s*[А-ЯЁа-яё]+\s*,?\s*[А-ЯЁа-яё]*,'
        pattern1 = r'^[А-ЯЁа-яё]+\s*,?\s*[А-ЯЁа-яё]+\s*,?\s*[А-ЯЁа-яё]*,.*'
        fio_pattern = r'^1,\2,\3,'#доработай тут
        result_del = re.split(pattern, fio_pattern, text)
        print(result_del)
        # result = re.findall(pattern, text)
        # print(result)
        # print(text)




