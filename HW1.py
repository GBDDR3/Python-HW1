# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
#  и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# a = int(input("Введите число от 1 до 7: \n"))

# if 1 <= a < 6:
#     print('нет')
# elif 6 <= a <= 7:
#    print('Да')
# else:
#   print('Введенo неправильное значение')


# ////////////////////////////////////////////////////////////////////

# Напишите программу, которая принимает на вход координаты точки
#  (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой
#   находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# y = int(input("Введите число y: \n"))
# x = int(input("Введите число x: \n"))

# if x > 0 and y > 0: print('1')
# elif x < 0 and y > 0: print('2')
# elif x < 0 and y < 0: print('3')
# elif x < 0 and y > 0: print('4')
# else: print("Введены неправильные значения")


# ///////////////////////////////////////////////////

# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

# number = int(input("Введите число от 1 до 4: \n"))

# if number == 1: print('x > 0, y > 0')
# elif number == 2: print('x < 0, y > 0')
# elif number == 3: print('x < 0, y < 0')
# elif number == 4: print('x > 0, y < 0')
# else: print("Введено неправильное значение")


# ///////////////////////////////////////////////////
# Напишите программу, которая принимает на вход координаты двух точек и находит 
# расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


# Ax = int(input("Введите число от не равное 0: \n"))
# Ay = int(input("Введите число от не равное 0: \n"))
# Bx = int(input("Введите число от не равное 0: \n"))
# By = int(input("Введите число от не равное 0: \n"))

# L = round(((Ax-Bx)**2+(Ay-By)**2)**0.5, 3)
# print(L)


# ////////////////////////////////////////////////////////////


# Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# x = int(input("Введите число от 0 до 1: \n"))
# y = int(input("Введите число от 0 до 1: \n"))
# z = int(input("Введите число от 0 до 1: \n"))

# c = -1*(x+y+z)
# d = -x*-y*-z

# if c < 0: c = 1
# if d < 0: d = 1

# if c == d: print("Утверждение истинно")
# else: print("Утверждение ложно")