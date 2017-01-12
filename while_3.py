#!/usr/bin/python
# -*- coding: utf-8 -*-

# Напишите цикл, выводящий ряд четных чисел от 0 до 20.
# Затем, каждое третье число в ряде от -1 до -21

i = 0
while i < 21:
    if i != 0 and i % 2 == 0:
        print i
        i += 1
    else:
        i += 1

i = 0
while i >= -21:
    if i != 0 and i % 3 == 0:
        print i
        i -= 1
    else:
        i -= 1
