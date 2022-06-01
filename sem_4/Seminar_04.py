#1.	Дан список чисел. Создать список, в который попадают числа, 
# описываемые возрастающую последовательность. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
# Порядок элементов менять нельзя

import random

n = int(input('Введите размерность заданного списка: '))

def compl_list(n):
    nums = []
    for i in range(n):
        nums.append(random.randint(1, 9))
    return nums

inst_list = compl_list(n)
print(inst_list)

def increasing(nums):
    incr = [nums[0]]
    for i in nums:
        if i > max(incr):
            incr.append(i)
    return incr
print(increasing(inst_list))


#2.	Создать и заполнить файл случайными целыми значениями. 
# Выполнить сортировку содержимого файла по возрастанию. 

import random

n = int(input('Введите количесвто случайных чисел: '))

def compl_list(n):
    nums = []
    for i in range(n):
        nums.append(random.randint(1, 9))
    return nums

rnd_nums = compl_list(n)
print(rnd_nums)
rnd_nums.sort()
print(rnd_nums)

path = 'rnd_nums.txt'

with open (path, 'w') as data:
    data.write(str(rnd_nums))

# 3.	Вот вам файл с тысячей чисел. Задача: найти триплеты и просто выводить их на экран. 
# Триплетом называются три числа, которые в сумме дают 0. 
# (решение будет долгим, ибо является демонстрационным при теме многопоточного программирования). 

nums = []
path = open('1Kints.txt', 'r')
for line in path:
    nums.append(int(line))

for i in range(len(nums) - 1):

    for j in range(len(nums) - 1):
        if nums[i] + nums[j] == 0:
            print('Первый триплет: ',nums[i], ' Второй триплет: ', nums[j])


    
