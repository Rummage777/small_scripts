#!/usr/bin/python
# -*- coding: utf-8 -*-


# Присвойте произвольную строку длиной 10-15 символов переменной и
# извлеките из нее следующие срезы:
# - первые восемь символов;
# - четыре символа из центра строки;
# - символы с индексами кратными трем.

word = raw_input('Write a sentence. You should use 10 - 15 symbols: ')
a = len(word)

while a < 10 or a > 15:
    if a < 10:
        print "Too small sentence. Please input longer one."
    elif a > 15:
        print "Too long sentence. Please input shorter one"
    word = raw_input('Please, enter a sentence: ')
    a = len(word)

word = word.upper()

middle = a / 2  # Округление не нужно потому что делим 2 int
first_eight = word[:8]
middle_four = word[middle - 2: middle + 2]

print "The length of your sentence is {}".format(a)
print "The first eigth letters are {}".format(first_eight)
print "The four letters in the middle are {}".format(middle_four)

every_third = ""
for i in xrange(1, a):
    if i % 3 == 0:
        every_third = every_third + word[i]
print "The third letters are {}".format(every_third)
