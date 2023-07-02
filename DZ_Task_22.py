# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
# i = int(input()) 
# list_1 = [i for i in range(1,10)]
# print(list_1)
import random

n = int(input('Введите количество элементов первого множества: '))
m = int(input('Введите количество элементов второго множества: '))
list_1 = set()
list_1 = set()
list_3 = set()
for i in range(n):
    list_1 =set(random.randint(0,10) for _  in range(n))

for j in range(m):
    list_2 =set(random.randint(0,10) for _  in range(m))
list_3 = sorted(list_1.intersection(list_2))
print(list_1)
print(list_2)
print(*list_3)