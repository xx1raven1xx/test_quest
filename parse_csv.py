# -*- coding: utf-8 -*-

import csv
import io
import shutil

path_csv = 'D:\\python\\test1\\test_data.csv'
path_test_data = shutil.copy(path_csv, 'D:\\python\\test1\\data.csv')
print(path_test_data)

greeting = ['здравствуйте', 'добрый день']
bye = ['до свидания', 'всего доброго']
my_name = ['меня зовут']


with io.open(path_test_data, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for rows in reader:
        list_lower = [row.lower() for row in rows]
        if list_lower[2] == 'manager':
            for greet in greeting:
                if greet in list_lower[3]:
                    print(list_lower)
            for b in bye:
                if b in list_lower[3]:
                    print(list_lower)

