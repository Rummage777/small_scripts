# !usr/bin/python3
# -*- coding: utf-8 -*-


'''
Присвойте произвольную строку длиной 10-15 символов переменной и извлеките из нее следующие срезы:
▪ первые восемь символов;
▪ четыре символа из центра строки;
▪ символы с индексами кратными трем.
'''

var_str = '1234567890ABCD'
first_eight = var_str[:8]
middle_four = var_str[6:10]
every_third = var_str[::3]

print(first_eight, middle_four, every_third)
