# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# lst = [2, 3, 5, 9, 3]


# def find_number(arg):
#   count = 0
#   for i in range(1, len(arg), 2):
#         count += arg[i]
#   return count

# number = find_number(lst)
# print(number)

# //////////////////////////////////////////////////////////////////////////

# # Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# # Пример:
# # - [2, 3, 4, 5, 6] => [12, 15, 16];
# # - [2, 3, 5, 6] => [12, 15]

# lst = [2, 6, 5, 8, 12]

# def find_list(arg):
#   lst1 = []
#   for i in range((len(arg) + 1) // 2):
#     a = arg[i]
#     b = arg[len(arg) - 1 - i]
#     lst1.append(a * b)
#   return lst1


# answer = find_list(lst)

# print(answer)


# /////////////////////////////////////////////////////////////////

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# # Пример:
# # - 45 -> 101101
# # - 3 -> 11
# # - 2 -> 10

# number = int(input("Введите число: \n"))


# def replase_number(arg):
#   count = ""  
#   while arg != 0:
#       count = str(arg%2) + count
#       arg = arg // 2
#   return count
  
# answer = replase_number(number)

# print(answer)


# /////////////////////////////////////////////////////

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

number = int(input("Введите число: \n"))

def fill_lst(arg):
   lst=[]
   f2 = f1 = 1
   for i in range(arg-1):
      с = 0
      lst.append(f2)
      с = f1 + f2 
      f2 = f1
      f1 = с
   return lst

  
def fill_list2(arg):
  c = 0
  c1 = 0
  c2 = 1
  lst1=[]
  for i in range(arg+1):
    lst1.append(c1)
    c = -1*(c1-c2)
    c2 = c1
    c1 = c
  lst1.reverse()
  return lst1
  

answer2 = fill_list2(number) + fill_lst(number)
print(answer2)