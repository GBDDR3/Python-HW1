# # Задание 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# # Пример:

# # 6782 -> 23
# # 0,56 -> 11

# number = input("Введите число: \n")
# count = 0

# def summ_number(arg):
#   count = 0
#   for i in arg:
#     if i == "." or i == ",":
#       continue
#     a = int(i)
#     count += a
#   return count

    
# answer = summ_number(number)

# print(answer)


# /////////////////////////////////////////////////////////


# # Задание 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# # Пример:

# # пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# number = int(input("Введите число: \n"))

# lst = []


# def factorial(arg):
#     count = 1
#     for i in range(1, arg + 1):
#         count *= i
#         lst.append(count)
#     return lst
  

# answer = factorial(number)
# print(answer)

# ///////////////////////////////////////////////////////


# # Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
# # округлённую до трёх знаков после точки.

# # Пример:

# # Для n = 6 -> 14.072

# number = int(input("Введите число: \n"))

# def summ_number(arg):
#     count = 0
#     sum = 0
#     for i in range(1, arg + 1):
   
#       count += (1 + 1 / i)**i
#     return round(count, 3)

# y = summ_number(number)
# print(y)


# ///////////////////////////////////////////////////////


# # Задание 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# # Найдите произведение элементов на позициях a и b.

# n = int(input("Введите значение n: \n"))
# a = int(input("Введите значение a(меньше n*2 + 1): \n"))
# b = int(input("Введите значение b(меньше n*2 + 1)): \n"))

# if a > n*2 + 1 or b > n*2 + 1:
#     raise TypeError("Введены не правильные значения")

# lst = []

# def fill_array(arg1, arg2, arg3):
#     c = 0
#     d = 0
#     for i in range(-n, n + 1):
#         lst.append(i)
#     c = lst[arg2 - 1]
#     d = lst[arg3 - 1]
#     return c * d
 

# y = fill_array(n, a, b)
# print(y)


# ////////////////////////////////////////////////////////////


# # Задание 5 Реализуйте алгоритм перемешивания списка.

# import random

# lst = [1, 2, 5, 8, 9, 12]
# lst1 = lst[:]

# def mix_array(arg):
#     lenght = len(arg)
#     for i in range(lenght):
#         case_number = random.randint(0, lenght-1)
#         temp = 0
#         temp = arg[i]
#         arg[i] = arg[case_number]
#         arg[case_number] = temp
#     return lst1


# y = mix_array(lst1)
# print(lst)
# print(y)