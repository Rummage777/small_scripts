#!/usr/bin/python
# -*- coding: utf-8 -*-

# Попытка написания unit-тестов для проверки правильности работы кода программы
n = 0

# Наборы тестовых данных с известным результатом
divider = "-" * 45
variables = [[1, 2, 1],
             [1, 1, 0],
             [6, 0, 0],
             [0, 0, 0],
             [1, 0, 1],
             [0, 2, 2],
             [0, 0, 9],
             [0, 7, 0],
             [1, 6, 9],
             [2, 4, 7]]

for i in xrange(10):
    a = variables[i][n]
    b = variables[i][n + 1]
    c = variables[i][n + 2]
    print "{} {} {}".format(a, b, c)

    print divider

    # Уравнение является квадратным
    if a != 0:
        discriminant = b ** 2 - 4 * a * c
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
    print "Test case # {}".format(i)
