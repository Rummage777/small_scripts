# !usr/bin/python3
# -*- coding: utf-8 -*-


'''
Придумайте программу, в которой из одной функции вызывается вторая. При этом ни одна из них ничего не возвращает в основную ветку программы, обе должны выводить результаты своей работы с помощью функции print().
'''


def count_sum(a, b):
    print('First sum =', a + b)


def count_result(a,b,c,d):
    count_sum(a, b)
    print('Second sum =', c + d)


count_result(10, 20, 17, 23)
