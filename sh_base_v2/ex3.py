# !usr/bin/python3
# -*- coding: utf-8 -*-

'''
Самостоятельно придумайте программу, в которой бы использовалась инструкция if (желательно с веткой else). Вложенный код должен содержать не менее трех выражений.
'''

input_data = {'fruit1': ('apple', 'green'),
              'fruit2': ('apple', 'yello'),
              'fruit3': ('apple', 'red'),
              'fruit4': ('apple', 'white'),
              'fruit5': ('banana', 'red'),
              'fruit6': ('orange', 'red'),
              'fruit7': ('banana', 'green'),
              'fruit8': ('orange', 'orange'),
              'fruit9': ('apple', 'green'),
              'fruit10': ('apple', 'yello'),
              'fruit11': ('apple', 'green'),
              'fruit12': ('apple', 'yello')}

def count_apples(data):
    count = {}
    for item in list(data):
        fruit = input_data[item]
        fruit_name = fruit[0]
        fruit_color = fruit[1]
        if fruit_name == 'apple':
            if fruit_color not in count:
                count[fruit_color] = 1
            else:
                count[fruit_color] += 1
    return count


print(count_apples(input_data))
