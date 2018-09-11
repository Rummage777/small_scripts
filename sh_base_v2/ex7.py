# !usr/bin/python3
# -*- coding: utf-8 -*-


'''
Напишите цикл, выводящий ряд четных чисел от 0 до 20. Затем, каждое третье число в ряде от -1 до -21
'''


def create_even_list():
    i = 0
    even_list = []

    while i <= 20:
        if i % 2 == 0 and i != 0:
            even_list.append(i)
        i += 1
    return even_list


def every_third_number_list():
    i = -1
    every_third_list = []
    while i >= -21:
        if i % 3 == 0:
            every_third_list.append(i)
        i -= 1
    return every_third_list


print(create_even_list())
print(every_third_number_list())


def test_even_list():
    result = create_even_list()
    if len(result) != 10:
        print('Test 1 failed')
    if sum(result) != 110:
        print('Test 2 failed')
    if result[0] != 2:
        print('Test 3 failed')
    if result[9] != 20:
        print('Test 1 failed')


test_even_list()


def test_every_third():
    result = every_third_number_list()
    if len(result) != 7:
        print('Test 1 failed')
    if result[0] != -3:
        print('Test 3 failed')
    if result[6] != -21:
        print('Test 1 failed')


test_every_third()
