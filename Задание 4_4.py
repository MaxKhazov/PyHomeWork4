#Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
import random

k = int(input("Введите большую степень многочлена: "))

list = []
for i in range(k):
    list.append(random.randint(0,100))
print (list)


with open('file.txt', 'a') as data:
    for i in list:
        data.writelines(str(i))
        data.writelines('x^')
        data.writelines(str(k))
        data.writelines('+')
        k -= 1
    data.writelines('\n')

