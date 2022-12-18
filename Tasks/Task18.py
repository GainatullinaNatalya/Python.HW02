# Реализуйте алгоритм перемешивания списка

list = []
for i in range(5):
    n = int(input('Введите число: '))
    list.append(n)
print(*list)
import random
random.shuffle(list)
print(*list)