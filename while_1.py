#!/usr/bin/python
# -*- coding: utf-8 -*-

# Написать программу, которая выводит ряд чисел Фибоначчи
# с первого по 20 член, с использованием оператора while.

i = 0
n_minus_1 = 0
n = 1
n_plus_1 = 0
print n_minus_1
print n

while i < 18:
    n_plus_1 = n_minus_1 + n
    print n_plus_1
    n_minus_1 = n
    n = n_plus_1
    i += 1
