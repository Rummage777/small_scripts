#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from collections import Counter

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

# new_meal = []
type_of_family = []

tips = 0.1
quantity_of_families = 3
number_of_meals = random.randint(1, 50)

divider_1 = " ".join("_" * 28)
divider_2 = "=" * 19

# Задаем меню ресторана, из которого можно выбрать блюда
name_of_meals = ['meal_{}'.format(i) for i in xrange(1, number_of_meals)]
prices_of_meals = [random.random() * 100 for i in xrange(1, number_of_meals)]
menu = dict(zip(name_of_meals, prices_of_meals))

# Задаем условия акции для расчета скидки
list_of_types = ['Small', 'Medium', 'Large']
size_of_discount = [0.02, 0.05, 0.1]
discount = dict(zip(list_of_types, size_of_discount))

for i in range(1, quantity_of_families + 1):
    total_order = []
    total_sum = 0.
    quantity_of_guests = 0

    # Задаем количество гостей в семье
    quantity_of_guests = random.randint(1, 10)

    # Задаем набор блюд в счете семьи
    for k in range(0, 3 * quantity_of_guests):
        new_meal = random.choice(name_of_meals)
        total_order.append(new_meal)
        total_sum = total_sum + menu[new_meal]
        bill = Counter(total_order)

    # Оформляем счет
    print divider_2 + " Family order №{} ".format(i) + divider_2
    print "Number of person {}".format(quantity_of_guests)
    print "Number of meals for family {}".format(3 * quantity_of_guests)
    print divider_1
    print "{:16}{:12}{}".format('Name of meal', 'Quantity', 'Price')
    print divider_1
    for k, price in menu.iteritems():
        if k > 0:
            print "{:16}{:d}{:16.2f}".format(k, bill[k], menu[k] * bill[k])
    print divider_1
    print "Total sum without discount  = {:.2f}".format(total_sum)

    # Применяем условия акционного предложения
    if 2 < quantity_of_guests <= 4:
        type_of_family = list_of_types[1]
        total_sum = total_sum - total_sum * discount.get(type_of_family)
    elif quantity_of_guests > 4:
        type_of_family = list_of_types[2]
        total_sum = total_sum - total_sum * discount.get(type_of_family)
    else:
        type_of_family = list_of_types[0]
        total_sum = total_sum + total_sum * tips - total_sum * \
            discount.get(type_of_family)
    print ("Famyly type - {}, discount value - {} percents".format
           (type_of_family, discount[type_of_family] * 100))
    print "Total sum with discount  = {:.2f}".format(total_sum)
