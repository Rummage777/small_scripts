# !usr/bin/python3
# -*- coding: utf-8 -*-


'''
3. Создайте список, содержащий элементы целочисленного типа, затем с помощью цикла перебора измените тип данных элементов на числа с плавающей точкой. (Подсказка: используйте встроенную функцию float().)

'''

sequence = [10, 20, 30, 40, 50]
i = 0
for item in sequence:
    sequence[i] = float(item)
    i += 1

print(*sequence)
