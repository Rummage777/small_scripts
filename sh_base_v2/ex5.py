# !usr/bin/python3
# -*- coding: utf-8 -*-

'''
Придумайте программу, в которой бы использовалась инструкция if-elif-else. Количество ветвей должно быть как минимум четыре.

Есть произвольная текстовая последовательность символов состоящая из NSEW, где буквы это команды роботу сделать 1 шаг:
    N - на север от текущего местоположения,
    S - на юг от текущего местоположения
    E - на восток от текущего местоположения
    W - на запад от текущего местоположения.

На старте робот стоит в положении 0,0 - это соответствует нижнему левому углу на краю карты.
Роботу за край карты выходить нельзя. Если произвольная последовательность команд дает указание выйти за границы карты, робот должен не подчиниться и написать: "Game over. Я покинул карту"
Если команда непонятна, то робот должен написать, что "Инструкция непонятна, жду следующую команду"
'''
orders = ('EENN', 'SSSS', 'WWWW', "QEEE", "edn8w37f7g", " D E E N N E W ")

def find_the_way(data):
    position = [0, 0]
    print('Command sequence =', data)
    for item in data:
        if item == 'N':
            position[0] += 1
        elif item == 'S':
            position[0] -= 1
        elif item == 'E':
            position[1] += 1
        elif item == 'W':
            position[1] -= 1
        elif item not in set("NSEW"):
            print('Инструкция непонятна, жду следующую команду')
            continue

        if position[0] < 0 or position[1] < 0:
            print('"Game over. Я покинул карту"')
            break
        else:
            print('New position = ', position)
            continue
    return position


for sequence in orders:
    result = find_the_way(sequence)
    print('Final position =', result)
    print()
    print()
