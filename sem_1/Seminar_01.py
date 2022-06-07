# Сформировать список из N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.

n = int(input("Введите количество членов поаледовательности: "))
nums =[(-3)**i for i in range(n)]
# for i in range(n) :
    
#     nums.append((-3)**i)
#     print(nums[i])

print(nums)
 
#Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 
# 3n + 1. Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n = int(input("Введите количество индекс значений: "))

# dictionary = []

# def element(x):
#     a = 3 * x +1
#     res = a
#     return res

# dictionary = {i : element(i) for i in range(n)}

# print(dictionary)

#Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

# s = str(input("Введите первую строку: "))
# t = str(input("Введите вторую строку: "))
 
# def str_count(str, substr):
#     return 0 if len(str) < len(substr) else str.startswith(substr) + str_count(str[1:], substr)
 
# print(str_count(s, t))

# #Подсчитать сумму цифр в вещественном числе.

# num = float(input("Введите вещественное число: "))

# def sum_num(num):
#     sum = 0
#     while num > 0:
#         sum += num % 10
#         num //= 10
#     return sum

# print(sum_num(num))

#Написать программу получающую набор произведений чисел от 1 до N. 
#Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

# n = int(input("Введите число n: "))

# def multi(n):
#     nums = [1]
#     for i in range(2, n + 1):
#         nums.append(nums[i - 2] * i)
      
#     return nums

# print(multi(n))