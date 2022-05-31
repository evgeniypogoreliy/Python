#1.	Найти НОК(наименьшее общее кратное) двух чисел

a = int(input("Введите перве число: "))
b = int(input("Введите второе число: "))

i = 1
while True:
    if i%a==0 and i%b==0:
      break
    i+=1
print(i)
    
#2.	Вычислить число Пи c заданной точностью d
#Пример: при d = 0.001,  c= 3.141.

import math

d = float(input("Введите необходимую точность числа Пи: "))

def count(num):
    s = str(num)
    if '.' in s:
        return abs(s.find('.') - len(s)) - 1
    else:
        return 0

n = round(math.pi, count(d))

print('Число Пи с указаонной точностью ', n)


#3.	Составить список простых множителей натурального числа N

n = int(input('Введите число N: '))

def factors(n):
    nums = []
    fact = [3, 4, 5, 6, 7, 8, 9]
    while n % 2 == 0:
        nums.append(2)
        n = n / 2
    for i in fact:
        while n % i == 0:
            nums.append(i)
            n = n / i
    if n > 2:
        nums.append(n)
    return nums

print(factors(n))

#4.	Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
#Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

import random
n = int(input('Введите размерность исходной последовательности: '))

def list_compl(n):
    worc_list = []
    for i in range(n):
        worc_list.append(random.randint(1, 9))
    return worc_list
first_list = list_compl(n)
print(first_list)

second_list = set(first_list)
print(second_list)

