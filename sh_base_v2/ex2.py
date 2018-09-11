# !usr/bin/python3
# -*- coding: utf-8 -*-


from math import sqrt

'''
Усовершенствуйте предыдущий код с помощью ветки else так, чтобы в зависимости от значения переменной, выводилась либо 1, либо -1.
'''


def find_apple(data):
    if 'apple' in data:
        return 1
    else:
        return -1


print(find_apple('apple, banana, orange'))
print(find_apple('banana, orange'))

def test():
    result = find_apple('grape')
    if result != -1:
        print('Test #1 failed')
    result = find_apple('grape, banana, apple')
    if result != 1:
        print('Test #2 failed')


test()
