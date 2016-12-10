#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

# Вычисление арифметического квадратного корня
# случайного числа по методу Герона

accuracy = 0.0001  # Задаем точность вычисления квадратного корня

counter = 0  # Счетчик количества итераций, требующихся для получения решения

# Генерируем случайное число, квадратных корень которого мы должны вычислить
x_int = random.randint(-100000, 100000)
x_decimal = x_int / 1000000
x = x_int + x_decimal
y = random.random()

# Выбираем будет ли Х целым или десятичным
if y >= 0.5:
    x = int(x)

# Проверяем существование у числа арифметического квадратного корня
if x < 0:
    print "У числа %d нет арифметического квадратного корня" % (x)

elif x == 0:
    print "Квадратный корень числа 0 равен 0"

else:
    guess = random.randint(1, 100)  # Генерируем число для 1-ой итерации

    # Сохраняем числа, которые проверяем в каждой итерации
    answer = []
    answer.append(guess)

    # Используем метод Герона
    while abs(x - guess**2) > accuracy:
        guess = 0.5 * (abs(guess) + float(x) / float(abs(guess)))
        answer.append(guess)
        counter += 1

    # Выводим результаты расчетов
    print "Звданная точность = %.4f" % (accuracy)
    print "Квадратный корень числа %.2f найден за %d шагов" % (x, counter + 1)
    print "Были проверены значения: " + '; '.join([str(a) for a in answer])
    print "Квадратный корень равен %.4f" % (answer[counter - 1])
