# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N

number = int(input('Введите число: '))
f = 1
for i in range(number - 1):
    i += 1
    f *= i
    print(f, end=', ')
print(f * number)