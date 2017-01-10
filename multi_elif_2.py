#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

# Придумайте программу, в которой бы использовалась инструкция
# if-elif-else
# Составить программу вычисления корней квадратного уравнения
# с использованием дискриминанта

divider = "-" * 45

for i in xrange(1, 11):
    a = random.randint(0, 2)
    b = random.randint(0, 1)
    c = random.randint(0, 1)
    print divider

    # Уравнение является квадратным
    if a != 0:
        discriminant = b ** 2 - 4 * a * c
        if b != 0:
            if c != 0:
                print "Equation #{} is {}*x^2 + {}*x + {} = 0".format(i, a, b, c)
            else:
                print "Equation #{} is {}*x^2 + {}*x = 0".format(i, a, b)
        else:
            if c != 0:
                print "Equation #{} is {}*x^2 + {} = 0".format(i, a, c)
            else:
                print "Equation #{} is {}*x^2 = 0".format(i, a)
        if discriminant > 0:
            x1 = (-b + discriminant ** 0.5) / (2 * a)
            x2 = (-b - discriminant ** 0.5) / (2 * a)
            print "Discriminant > 0"
            print "Roots are: x1 = {:.2f}, x2 = {:.2f}".format(x1, x2) + "\n"
        elif discriminant < 0:
            print "Discriminant < 0"
            print "Equation #{} has no roots".format(i) + "\n"
        else:
            x = -b / (2 * a)
            print "Discriminant = 0"
            print "Root is single: x = {}".format(x) + "\n"

    # Получившееся выражение не является уравнением
    elif b == 0:
        print "Expresion #{} is not an equation".format(i)
        print "Root doesn't exist" + "\n"

    # Уравнение является линейным
    else:
        if c == 0:
            x = 0
            print "Equation #{} is {}*x = 0".format(i, b)
        else:
            x = -c / b
            print "Equation #{} is {}*x + {} = 0".format(i, b, c)
        print "Expresion #{} is linear equation".format(i)
        print "Root is single: x = {}".format(x) + "\n"
