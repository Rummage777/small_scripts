# !usr/bin/python3
# -*- coding: utf-8 -*-


'''
Напишите скрипт на языке программирования Python, выводящий ряд чисел Фибоначчи (см. пример выше). Запустите его на выполнение. Затем измените код так, чтобы выводился ряд чисел Фибоначчи, начиная с пятого члена ряда и заканчивая двадцатым.
'''

def fibonacci(a,b):
    result = []
    result.append(a)
    result.append(b)
    i = 2
    while i < 20:
        result.append(result[i-1] + result[i-2])
        i += 1
    return result


print(fibonacci(0,1))


def test_fibonacci():
    func = fibonacci(0,1)
    if len(func) != 20:
        print('Test #1 failed')
    if func[5] != 5:
        print('Test #2 failed')
    if func[19] == 4180:
        print('Test #3 failed')


test_fibonacci()
