# Задача 22: 
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

# Решение:

from random import randint

numb = int(input('Введите количество элементов первого множества: '))
numb1 = int(input('Введите количество элементов второго множества: '))

set_numbers = []
set_numbers_1 = []
set_numbers_2 = []

# Заполняю список рандомными числами.
for i in range(numb):
    result = randint(0, numb) 
    set_numbers.append(result)
for i in range(numb1):
    result = randint(0, numb1) 
    set_numbers_1.append(result)

# Для объединения списков применяется операция сложения (+):
set_numbers_2 = set_numbers + set_numbers_1

# использовать встроенную функцию set() для преобразования списка в набор, 
# а затем использовать функцию list(), 
# чтобы преобразовать его обратно в список.
set_numbers_2 = list(set(set_numbers_2)) 

print(set_numbers, "\n", set_numbers_1, "\n", set_numbers_2)