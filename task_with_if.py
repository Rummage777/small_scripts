#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import math

# 1. Написать код, в к-ом в случае, если значение некой переменной
# больше 0, то выводится специальное сообщение. Выполнить программу
# несколько раз при значении переменной > 0 и < 0
# 2. Использовать в коде ветку else так, чтобы в зависимости от
# значений переменной  на определенном шаге выводилось либо 1, либо -1.

attempt = 0
counter = 0
x = 0

while attempt < 10:
    attempt += 1
    x = random.uniform(-1, 1)
    if x > 0:
        x = math.ceil(x)
        print "Попытка №%.2i Х положительное число" % (attempt)
        counter += 1
    else:
        x = math.floor(x)
    print x
print "ИТОГИ: Из %i попыток %i чисел положительные" % (attempt, counter)
