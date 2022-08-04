# Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности.
import random

N = int(input('Введите количество символов в списке: '))
list = []
newlist = []

for i in range(N):
    list.append(random.randint(0,10))

for i in list:
    if list.count(i) == 1:
        newlist.append(i)
print(list)
print(newlist)

