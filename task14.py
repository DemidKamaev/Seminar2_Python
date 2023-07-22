# Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числа вида 2k), не превосходящие числа N.


step = 0
result = 1
N = int(input("Введите число: "))
while result <= N:
    print(result)
    step += 1
    result *= 2

# result = 2 ** step