# !usr/bin/python3
# -*- coding: utf-8 -*-

from math import sqrt

'''
Напишите программный код, в котором в случае, если значение некой переменной больше 0, выводилось бы специальное сообщение (используйте функцию print). Один раз выполните программу при значении переменной больше 0, второй раз — меньше 0.
'''


def calculate_root(data):
    if data < 0:
        return 'Number must be > 0'
    else:
        return sqrt(data)


print(calculate_root(-100))
print(calculate_root(100))
