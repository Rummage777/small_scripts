#!usr/bin/python
# -*- coding: utf-8 -*-

# Перепишите предыдущую программу так, чтобы пользователю
# предлагалось решать пример до тех пор, пока он не напишет
# правильный ответ. (При решении задачи используйте цикл while.)
answer = None
print 'Solve the problem: 4*100 - 54. '

while answer != 346:
    answer = raw_input('Print the answer  ')
    if answer.isdigit() is False:
        print "Wrong input. You should print only digits"
    else:
        answer = int(answer)
        if answer != 346:
            print "Answer is incorrect. Try again!"
print "You are brilliant! Answer is correct!"
