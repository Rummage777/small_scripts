#!usr/bin/python
# -*- coding: utf-8 -*-

# Перепишите предыдущую программу так, чтобы пользователю
# предлагалось решать пример до тех пор, пока он не напишет
# правильный ответ. (При решении задачи используйте цикл while.)

answer = raw_input('Solve the problem: 4*100 - 54. ')
while answer.isdigit() is False:
    print "Wrong input. You should print only digits"
    answer = raw_input('Print the answer  ')

answer = int(answer)
while answer != 346:
    print "Answer is incorrect. Try again!"
    answer = raw_input('Print the answer  ')
    answer = int(answer)
print "You are brilliant! Answer is correct!"
