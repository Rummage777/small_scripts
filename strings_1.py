#!/usr/bin/python
# -*- coding: utf-8 -*-

# Свяжите переменную с любой строкой, состоящей не менее
# чем из 8 символов. Извлеките из строки первый символ,
# затем последний, третий с начала и третий с конца.
# Измерьте длину вашей строки.

word = raw_input('Write a word. You should use 8 or more symbols: ')
a = len(word)

while a < 8 or word.isalpha() is not True:
    if a < 8:
        print "Too small word. Please input longer one."
    elif word.isalpha() is not True:
        print "Numbers and spaces are forbidden. Letters only."
    word = raw_input('Please, enter a word: ')
    a = len(word)

word = word.upper()

first = word[0]
last = word[-1]
third_start = word[2]
third_end = word[-3]

print "The length of your word is {}".format(a)
print "The first letter in your word is {}".format(first)
print "The last letter in your word is {}".format(last)
print "The third letter from the begining is {}".format(third_start)
print "The third letter from the end is {}".format(third_end)
