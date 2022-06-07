#Найти сумму чисел списка стоящих на нечетной позиции
#Пример:[1,2,3,4] -> 4

# import random
# n = int(input("Введите размерность списка: "))

# def list_compl(n):
#     nums =[]
#     for i in range(n):
#         nums.append(random.randint(1, 9))
#     return nums

# def sum(list):
#     sum = 0
#     for i in range(len(list)):
#         if i % 2 == 1:
#             sum = sum + list[i]
#     return sum
# res_list = list_compl(n) 
# print(res_list)
# print(sum(res_list))
#______________________________________________________

# nums = [random.randint(1, 9) for i in range(n)]
# print(nums)
# res = [nums[i] for i in range(len(nums)) if i % 2]
# print(sum(res))


#Найти произведение пар чисел в списке. Парой считаем первый и последний элемент,
#второй и предпоследний и т.д. 
#Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

# import random
# import math
# n = int(input("Введите размерность списка: "))

# def list_compl(n):
#     nums = []
#     for i in range(n):
#         nums.append(random.randint(1, 9))
#     return nums

# work_list = list_compl(n)

# def multi_duo(list):
    
#     res_list = []
#     for i in range(math.ceil(len(list)/2)):
#         res_list.append(list[i]*list[-i-1])
#     return res_list
# print(work_list)
# print(multi_duo(work_list))
#_____________________________________________

# nums = [random.randint(1, 9) for i in range(n)]
# print(nums)
# duo_nums = [nums[i]*nums[-i-1] for i in range(math.ceil(len(nums)/2))]
# print(duo_nums)

#В заданном списке вещественных чисел найдите разницу между максимальным и 
# минимальным значением дробной части элементов. 
#Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# from random import uniform

# n = int(input("Введите размерность списка: "))

# def list_compl(n):
#     worc_list = []
#     for i in range(n):
#         worc_list.append(round(uniform(0.01, 9.99), 2))
#     return worc_list

# list_f = list_compl(n)

# def max_min(list):
#     min = list[0] - int(list[0]) 
#     max = list[1] - int(list[1])
#     for i in range(len(list)):
#         if (list[i]- int(list[i])) < min :
#             min = (list[i]- int(list[i]))
#         if (list[i]- int(list[i])) > max:
#             max = (list[i]- int(list[i]))
#     return max - min

# print(list_f)
# print(max_min(list_f))

#Написать программу преобразования десятичного числа в двоичное

# a = int(input("Введите десятичное число: "))

# def dec_bin(num):
#     bin_num = []
#     while num > 0:
#         bin_num.insert(0, num % 2)
#         num = num // 2
#     return bin_num

# print(dec_bin(a))
