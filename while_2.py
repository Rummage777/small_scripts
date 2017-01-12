#!/usr/bin/python
# -*- coding: utf-8 -*-

# Написать программу, которая выводит ряд чисел Фибоначчи
# с 5 по 30 член, с использованием оператора while.

i = 0
n_minus_1 = 3
n = 5
n_plus_1 = 0
print n_minus_1
print n

while i < 23:
    n_plus_1 = n_minus_1 + n
    print n_plus_1
    n_minus_1 = n
    n = n_plus_1
    i += 1
