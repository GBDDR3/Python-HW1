
# //////////////////////////////////////////////////////////////////////////////////////////////////////

# 2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# number = int(input("Введите число: \n"))

# def find_number(arg):
#     const = 2
#     lst = []

#     while const <= arg:
#         if arg % const == 0:
#             lst.append(const)
#             arg //= const
#         else:
#             const += 1
#     return lst

# print(find_number(number))

# *Пример*

# - при N=236     ->        [2, 2, 59]

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////


# 3 Задайте последовательность чисел. Напишите программу, которая выведет список
#  неповторяющихся элементов исходной последовательности.

# *Пример*

# - при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]


# lst = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]
# number = int(input("Введите количество повторяющихся значений: \n"))


# def fill_list(arg, arg2):
#     lst1=[]
#     for i in range(len(arg)):
#         if arg.count(arg[i]) == arg2:
#             lst1.append(arg[i])
#     return lst1


# print(fill_list(lst, number))

# //////////////////////////////////////////////////////////////////////////

# 4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.

# *Пример:* 

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


from random import randint

k = int(input("Введите натуральную степень k = "))

def create_list(arg):
    lst = [randint(0,101) for i in range(1, arg+1)]
    return lst


def create_eq(arg):
    lst = arg[::-1]
    eq = " "
    if len(arg) < 0:
        eq = "x = 0"
    else:
        for i in range(len(lst)):
            if i != len(lst) - 2 and i != len(lst) - 1 and lst[i] != 0:
                eq += f'{lst[i]}z^{len(lst)-i-1}'
                if lst[i + 1] != 0:
                    eq += " + " 
            elif i == len(lst) - 2 and lst[i] != 0:
                 eq += f"{lst[i]}x"
                 if lst[i + 1] != 0:
                    eq += " + " 
            elif i == len(lst) - 1 and lst[i] != 0:  #elif i == len(lst) - 1 and lst[i] != 0
                 eq += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:  #elif i == len(lst) - 1 and lst[i] == 0
                    eq += " = 0"
    return eq



def write_file(arg):
    with open ("HW4.txt", "w", encoding = "utf-8") as file:
        file.write(arg)

write_file(create_eq(create_list(k)))
