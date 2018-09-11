# !usr/bin/python3
# -*- coding: utf-8 -*-


'''
Создайте скрипт (файл data.py), который бы запрашивал у пользователя - его имя: "What is your name?"
- возраст: "How old are you?"
- место жительства: "Where are you live?"
, а затем выводил три строки
- "This is имя"
- "It is возраст"
- "He lives in место_жительства"
, где вместо имя, возраст, место_жительства должны быть соответствующие данные, введенные пользователем.
'''


def print_data(name, age, location):
    print('This is {}'.format(name))
    print('He is {} years old'.format(age))
    print('He lives in {}'.format(location))


print_data(name=input('What is your name? '), age=input('How old are you? '), location =input('Where do you live? '))
