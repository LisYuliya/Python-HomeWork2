'''Реализуйте алгоритм перемешивания списка.'''

import random

lenght = int(input('Введите длину списка: '))
some_list = []

for i in range(0, lenght):

    n = int(input('Введите число: '))
    some_list.append(n)

print('Список: ', some_list)
random.shuffle(some_list)
print('Перемешанный список: ', some_list)
