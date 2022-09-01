# -*- coding: utf-8 -*-

import csv
import io

greeting = ['здравствуйте', 'добрый день']
bye = ['до свидания', 'всего доброго']

path_csv = 'D:\\python\\test1\\test_data.csv'

with io.open(path_csv, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for rows in reader:
        list_lower = [row.lower() for row in rows]
        if list_lower[2] == 'manager':
            if greeting[0] in list_lower[3]:
                print(list_lower)
            if greeting[1] in list_lower[3]:
                print(list_lower)
            if bye[0] in list_lower[3]:
                print(list_lower)
            if bye[1] in list_lower[3]:
                print(list_lower)
            #if (for greet in greeting) in list_lower[3]:
