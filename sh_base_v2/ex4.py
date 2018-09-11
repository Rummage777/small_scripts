# !usr/bin/python3
# -*- coding: utf-8 -*-

import random

'''
Напишите программу по следующему описанию:
a. двум переменным присваиваются числовые значения;
b. если значение первой переменной больше второй, то найти разницу значений переменных (вычесть из первой вторую), результат связать с третьей переменной;
c. если первая переменная имеет меньшее значение, чем вторая, то третью переменную связать с результатом суммы значений двух первых переменных;
d. во всех остальных случаях, присвоить третьей переменной значение
первой переменной;
e. вывести значение третьей переменной на экран.
'''


def count_third(first, second):
    print('First = {}, Second = {}'. format(first, second))
    if first > second:
        third = first - second
    elif first < second:
        third = first + second
    else:
        third = first

    return third


print(count_third(int(random.random() * 10), int(random.random() * 10)))


def test_third():
    print('Tests started:')
    result = count_third(3, 1)
    print(result)
    if result != 2:
        print('Test #1 failed')
    result = count_third(1, 3)
    print(result)
    if result != 4:
        print('Test #2 failed')
    result = count_third(1, 1)
    print(result)
    if result != 1:
        print('Test #3 failed')

test_third()
