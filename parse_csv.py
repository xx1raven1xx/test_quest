# -*- coding: utf-8 -*-

import csv
import io
from operator import index
import shutil
from natasha import NamesExtractor, MorphVocab


path_csv = 'D:\\python\\test1\\test_data.csv'
path_test_data = shutil.copy(path_csv, 'D:\\python\\test1\\data.csv')
# print(path_test_data)

greeting = ['здравствуйте', 'добрый день']
bye = ['до свидания', 'всего доброго']
my_name = ['меня зовут']

morph_vocab = MorphVocab()
extractor = NamesExtractor(morph_vocab)
# matches = extractor(text)
# for match in matches:
#     start, stop = match.span
#     print(start, stop, text[start:stop])
#     print(match.fact)
#     print()

with io.open(path_test_data, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for rows in reader:
        matches = extractor(rows)

        print(str(matches)) # нужно откорректировать данный вывод. Не работает.
        list_lower = [row.lower() for row in rows]
        if my_name[0] in list_lower[3]:
            print(list_lower)
        # if list_lower[2] == 'manager':
        #     for greet in greeting:
        #         if greet in list_lower[3]:
        #             print(list_lower)
        #     for b in bye:
        #         if b in list_lower[3]:
        #             print(list_lower)

