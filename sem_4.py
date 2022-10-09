# Задача 1. Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# d = float (input ('точность d = '))
# count =0
# while (d !=1):
#     d *= 10
#     count +=1
# print (count)
# import math
# x = round (math.pi, count)
# print (x)

# Задача 2. Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.


# def simple_num(x):
#     i = 2
#     lst_simple = []
#     while i*i <= x:
#         while x%i == 0:
#             lst_simple.append(i)
#             x = x/i
#         i = i+1
#     if x > 1:
#        lst_simple.append(int(x))
#     return lst_simple

# n = int (input ('задайте число n= '))
# print (simple_num(n))

# Задача 3. Задать последовательность чисел.
# Написать программу, которая выведет список неповторяющихся элементов
# import random

# lst = []
# for i in range (10):
#     lst.append(random.randint(1,10))
# print (lst)
# lst2 = []

# count =0
# for i in lst:
#     if lst.count(i) == 1:
#         lst2.append(i)

# print (lst2)
    
# Задача 4. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и 
# записать в файл многочлен степени k.

# import random
# k = int (input ('введите k= '))
# s = ""
# for i in range (0, k+1):
#     s = str(random.randint(0,101)) + 'x^'+ str(i) + s
#     if i != k: s = '+' + s
# print(s)

# Задача 5. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

s1 = "3x^2+2x+5"
s2 = "5x^2+4x+7"
a1 =s1.split('x')[0]
a11 = int(a1)
# print (a11)
s12 = s1[s1.find("+")+1:]
b1 = s12.split('x')[0]
b11 = int (b1)
# print (b11)
s13 = s12[s12.find("+")+1:]
c1 = int (s13)
# print (c1)

a2 =s2.split('x')[0]
a22 = int(a2)
# print (a22)
s22 = s2[s2.find("+")+1:]
b2 = s22.split('x')[0]
b22 = int (b2)
# print (b22)
s23 = s22[s22.find("+")+1:]
c2 = int (s23)
# print (c2)

q = a11+a22
print (q)
w = b11+b22
print (w)
e = c1+c2
print (e)

print (f'{q}x^2+{w}x+{e}')


