#!/usr/bin/python
# -*- coding: utf-8 -*-

# Напишите программу (файл example.py), которая предлагала
# бы пользователю решить пример 4*100-54. Если пользователь
# напишет правильный ответ, то получит поздравление от
# программы, иначе – программа сообщит ему об ошибке.
# (При решении задачи используйте конструкцию if-else.)

answer = raw_input('Solve the problem: 4*100 - 54. You have one attempt ')
if answer.isdigit() is True:
    answer = int(answer)
    if answer == 346:
        print "You are brilliant! Answer is correct!"
    else:
        print "Nice try! Answer is incorrect."
else:
    print "Wrong input. You should print only digits"
