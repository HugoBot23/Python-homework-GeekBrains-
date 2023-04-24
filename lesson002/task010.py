# На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
# С клавиатуры вводятся число монет и сами монеты построчно.

# Пример:
# Ввод: 1 1 1 1 0 0 -> 2

# РЕШЕНИЕ №1

from random import randint

numb_coins = int(input('Введите количество монет: '))
eagle = 0
count = 0

for i in range(numb_coins):
    coins = randint(0, 1)
    print(coins)
    if coins == eagle:
        count += 1
print('Количество монет которые нужно перевернуть:', count)


# РЕШЕНИЕ №2

# from random import randint

# numb_coins = int(input('Введите количество монет: '))
# eagle = 0
# count = 0
# list_coins = []

# for i in range(numb_coins):
#     coins = randint(0, 1)
#     list_coins.append(coins)
# print(list_coins)

# for i in list_coins:
#     if i == eagle:
#         count += 1
# print('Количество монет которые нужно перевернуть:', count, i)

# РЕШЕНИЕ №3

# numb_coins = int(input('Введите количество монет: '))
# eagle = 0
# count = 0
# list_coins = []
# print('Введите в каком порядке у вас лежат монеты где 1-орешко 0-орел:')
# for i in range(numb_coins):
#     list_coins.append(int(input()))
# print(list_coins)

# for i in list_coins:
#     if i == eagle:
#         count += 1
# print('Количество монет которые нужно перевернуть:', count)

# РЕШЕНИЕ №4

# numb_coins = int(input('Введите количество монет: '))
# eagle = 0
# count = 0
# print('Введите в каком порядке у вас лежат монеты где 1-орешко 0-орел:')
# for i in range(numb_coins):
#     coins = input()
#     if eagle == int(coins):
#         count += 1
# print('Количество монет которые нужно перевернуть:', count)
