# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# *Пример:*

# 2 2
#     4 

n = int(input('Введите первое целое число: '))
m = int(input('Введите второе целое число: '))

def sum(n,m):
    if n == 0:
        return m
    else:    
        return sum(n - 1, m + 1)
print(sum(n,m))    

    