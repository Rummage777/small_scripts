# !usr/bin/python3
# -*- coding: utf-8 -*-


'''
Самостоятельно придумайте программу на Python, в которой бы использовался цикл while. Пипец какой ленивый препод!
'''

input_data = 'Самостоятельно придумайте программу на Python, в которой бы использовался цикл while. Пипец какой ленивый препод!'


def count_while_find_end(data):
    '''Считать знаки до конца предложения. Вывести количество знаков в предложении'''
    count = 0
    item = ''
    while item != '.':
        item = data[count]
        if item != '.':
            count += 1
    return count


print(count_while_find_end(input_data))


def test_count_while():
    count = count_while_find_end('Hello world.')
    if count != 11:
        print(count)
        print('Test 1 failed')


test_count_while()
