'''Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

Пример:

- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)'''

num = int(input('Введите число: '))
factorial = 1
some_list = []

for i in range(2, num+1):
    some_list.append(factorial)
    factorial *= i
    
some_list.append(factorial)
print(some_list)
