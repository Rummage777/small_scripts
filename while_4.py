#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

# С использованием while написать программу,
# которая будет угадывать случайное число от 1 до 100
# с наименьшим количеством попыток

for i in range(1, 11):
    counter = 0
    floor = 1
    cell = 100
    unknown_number = random.randint(floor, cell)
    print "=" * 10 + "Game #{}".format(i) + "=" * 10
    while floor != cell:
        if unknown_number < (floor + cell) // 2:
            cell = (floor + cell) // 2
            print "Number < {}".format(cell)
            counter += 1
        elif unknown_number == (floor + cell) // 2:
            floor = (floor + cell) // 2
            counter += 1
            break
        else:
            floor = (floor + cell) // 2 + 1
            print "Number is > {}".format(floor)
            counter += 1
    print "Attempt #{}. Answer is {}".format(counter, floor) + "\n"
