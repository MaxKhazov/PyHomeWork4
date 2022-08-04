# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
n = int(input('Введите число, которое хотите разложить на множители: '))

def mnozhitel(n):
    list = []
    x = 2
    while x * x <= n:
        if n % x == 0:
            list.append(x)
            n = n // x
        else:
            x += 1
    if n > 1:
        list.append(n)
    return list
print(mnozhitel(n))
