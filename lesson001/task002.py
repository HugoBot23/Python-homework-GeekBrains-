# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

print('Введите трехзначное число: ')
number = int(input())

summa = 0

remains1 = number % 10
summa = summa + remains1
number = number // 10

remains2 = number % 10
summa = summa + remains2
number = number // 10

summa = summa + number

print(summa)
