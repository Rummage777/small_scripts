#!/usr/bin/python
# -*- coding: utf-8 -*-

# Исходные координаты тестовых заданий CodinfGame
# Координаты Алтаря молний: testcases_light_x, testcases_ligth_y
# Оставшееся количество шагов Тора: testcases_energy
# Координаты Тора: testcases_Thor_x, testcases_Thor_y
testcases_light_x = [31, 31, 0, 36]
testcases_ligth_y = [4, 4, 17, 17]

testcases_energy = [100, 13, 44, 36]

testcases_Thor_x = [5, 31, 31, 0]
testcases_Thor_y = [4, 17, 4, 0]
result = None
move_x = None
move_y = None

# Подставляем исходные данные из тест кейсов CodinfGame
for i in range(0, 4):
    light_x = testcases_light_x[i]
    light_y = testcases_ligth_y[i]
    x = testcases_Thor_x[i]
    y = testcases_Thor_y[i]
    energy = testcases_energy[i]
    i += 1
    print "Test № %d" % (i)

# Цикл игры: Тор выбирает направлениев котором делает ход и выполняет ход
    while energy > 0:
        energy -= 1

        move_x = ""
        move_y = ""

        if y > light_y:
            y -= 1
            move_y = "N"

        if y < light_y:
            y += 1
            move_y = "S"

        if x > light_x:
            x -= 1
            move_x = "W"

        elif x < light_x:
            x += 1
            move_x = "E"

# В блоке проверяем соблюдение условий победы и поражения в игре
# и печатаем причины поражения для анализа и отладки
        if x < 0 or y < 0 or x > 39 or y > 17 or energy < 0:
            result = "Thor is dead! END GAME"

        elif x == light_x and y == light_y:
            result = "Thor is WIN!!!"

        if result is not None:
            print result
            if result == "Thor is dead! END GAME":
                print "Выпал с карты по x < 0 " + str(x < 0)
                print "Выпал с карты по y < 0 " + str(y < 0)
                print "Выпал с карты по x > 39 " + str(x > 39)
                print "Выпал с карты по y > 17 " + str(y > 17)
                print "Закончилась энергия " + str(energy == 0)
            result = None
            break

# Даем команду куда сделать следующий шаг
        print str(move_y) + str(move_x)
