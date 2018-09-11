# !usr/bin/python3
# -*- coding: utf-8 -*-


'''
2. Измените предыдущую программу так, чтобы в конце каждой буквы строки добавлялось тире. (Подсказка: цикл for может быть вложен в другой цикл.)


'''

sequence = ['first', 'second', 'third', 'fourth']

for item in sequence:
    for char in item:
        print(char, end='-')
