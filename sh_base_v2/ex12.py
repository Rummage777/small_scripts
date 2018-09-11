# !usr/bin/python3
# -*- coding: utf-8 -*-


'''
Свяжите переменную с любой строкой, состоящей не менее чем из 8 символов. Извлеките из строки первый символ, затем последний, третий с начала и третий с конца. Измерьте длину вашей строки.
'''

var_str = 'Свяжите переменную с любой строкой, состоящей не менее чем из 8 символов.'
first = var_str[0]
last = var_str[-1]
third = var_str[2]
reversed_third = var_str[-3]


print(first, last, third, reversed_third)
print('lenght =', len(var_str))
