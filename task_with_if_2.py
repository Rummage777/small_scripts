#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

# Придумайте программу, в которой используется инструкция if c ветками
# elif и else.
# Вложенный код должен содержать не менее 3 выражений.

# Рассчитать сумму заказа в ресторане по акции и распечатать чек.
# Условия акции зависят от размера семьи.
# Каждый член семьи заказывает 3 случайных блюда
# Маленькая семья (2 или меньше человек) должна платить 10% чаевых. Скидка - 2%
# от суммы заказа без чаевых.
# Средняя семья (3-4 человека) не платят чаевые и получают скидку 5% от суммы
# заказа.
# Большая семья (5 и более человек) не платят чаевые и получают скидку
# 10% от суммы заказа

i = 0
total_summ = 0.00
total_order = []
number_of_meals = 0
quantity_of_guests = 0
family_order = []
type_of_family = []

divider = "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _"

tips = 0.1
quantity_of_families = 3

# Задаем меню ресторана, из которого можно выбрать блюда
name_of_meals = ["Meal_1", "Meal_2", "Meal_3", "Meal_4", "Meal_5", "Meal_6"]
prices_of_meals = [1.00, 2.00, 3.00, 4.00, 5.00, 6.00]
menu = dict(zip(name_of_meals, prices_of_meals))

# Задаем условия акции для расчета скидки
family_size = ["Small", "Medium", "Large"]
value_of_discount = [0.02, 0.05, 0.1]
discount = dict(zip(family_size, value_of_discount))


for i in range(1, quantity_of_families):
    print "=================== Famyly order № %i ====================" % (i)
    quantity_of_guests = random.randint(1, 3)
    number_of_meals = 3 * quantity_of_guests

    # Определяем набор блюд в счете
    for k in range(0, number_of_meals):
        total_order.append(random.choice(name_of_meals))
        total_summ = total_summ + menu[total_order[k]]

    # Оформляем счет
    print "Number of person %i" % (quantity_of_guests)
    print "Number of meals for family %i" % (number_of_meals)
    print divider
    print "Name of meal   Quantity    Price"
    print divider
    for k in name_of_meals:
        bill = total_order.count(k)
        if bill > 0:
            print (str(k) + "         " + str(bill) +
                  "           " + "%.2f" % (menu[k] * bill))
    print divider
    print "Сумма заказа без скидки  = " + str(total_summ)

    # Применяем акционные условия
    if 2 < quantity_of_guests <= 4:
        type_of_family = family_size[1]
        total_summ = total_summ - total_summ * discount[type_of_family]
    elif quantity_of_guests > 4:
        type_of_family = family_size[2]
        total_summ = total_summ - total_summ * discount[type_of_family]
    else:
        type_of_family = family_size[0]
        total_summ = total_summ + total_summ * tips - total_summ * discount[type_of_family]
    print ("Famyly type - %s, размер скидки - %i процентов" %
          (type_of_family, discount[type_of_family] * 100))
    print "Сумма заказа со скидкой  = " + str(total_summ)
    print
    print
    total_order = []
    total_summ = 0
