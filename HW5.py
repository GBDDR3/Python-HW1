# #1. Напишите программу, удаляющую из текста все слова, содержащие "еч".

# t = "В траве сидел кузнечик, в траве сидел кузнечик, cовсем как огуречик. Зелененький он был. Представьте себе, представьте себе — совсем как огуречик, представьте себе, представьте себе — зелененький он был!"

# text = t.split()

# itog = list(filter(lambda e: "еч" not in e, text))

# print(itog)

# /////////////////////////////////////////////////////////////////////////////////////////////////////



# 2 Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
#  Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
#  Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


# from random import randint

# quantity = int(input("Введите количество конфет: \n"))

# player = randint(1,2)

# print(f"Игрок {player} начинает игру")

# while quantity % 28 != 0 or quantity // 28 == 0:
#   number = input(f"Игрок {player}. Введите количество конфет: \n")
#   if number.isdigit() == False:
#     print("Количество пишется в цифрах, а не в буквах!!!! Введи цифру!")
#     number = int(input(f"Игрок {player}. Введите количество конфет: \n"))
#   quantity -= int(number)
#   if quantity <= 0:
#     print("Игра закончена. Вы победили")
#     break
#   print(quantity)

#   number1 = input("Следующий игрок. Введите количество конфет: \n")
#   if int(number) < 0:
#     print("Введена дробная или отрицательная цифра!!!")
#     number1 = int(input("Следующий игрок.. Введите количество конфет: \n"))
#   quantity -= int(number)
  
#   if quantity <= 0:
#     print("Игра закончена. Вы победили")
#     break
#   print(quantity)


#   //////////////////////////////////////////////////////////////////////////////////////////////////////////


# 3. Создайте программу для игры в ""Крестики-нолики""


# from random import randint

# field = [ "1", "2", "3",
#           "4", "5", "6",
#           "7", "8", "9"]

# print("  ", field[0], field[1], field[2],"\n"," ",field[3], field[4], field[5], "\n"," ", field[6], field[7], field[8])


# player = randint(1,2)

# print(f"Игрок {player} начинает игру")

# for i in range(len(field) // 2):
#     number = int(input("Введите число, вместо которого нужно поставить a: \n"))
#     field[number - 1] = "a"
#     print("  ", field[0], field[1], field[2],"\n"," ",field[3], field[4], field[5], "\n"," ", field[6], field[7], field[8])
#     if (field[0]==field[1]==field[2] or field[0]==field[3]==field[6] or field[0]==field[4]==field[8] or field[1]==field[4]==field[7] or
#      field[2]==field[5]==field[8] or field[3]==field[4]==field[5] or field[2]==field[4]==field[6] or field[6]==field[7]==field[8]):
#         print("Игра остановлена. Вы выйграли")
#         break
#     number1 = int(input("Введите число, вместо которого нужно поставить b: \n"))
#     field[number1 - 1] = "b"
#     print("  ", field[0], field[1], field[2],"\n"," ",field[3], field[4], field[5], "\n"," ", field[6], field[7], field[8])
#     if (field[0]==field[1]==field[2] or field[0]==field[3]==field[6] or field[0]==field[4]==field[8] or field[1]==field[4]==field[7] or
#     field[2]==field[5]==field[8] or field[3]==field[4]==field[5] or field[2]==field[4]==field[6] or field[6]==field[7]==field[8]):
#         print("Игра остановлена. Вы выйграли")
#         break
# else:
#     print("Игра остановлена. Ничья")

# //////////////////////////////////////////////////////////////////////////////////////////////

# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


# string = "eeeetttttttuuuuuuuqqqqq"
# count = 1
# string_mini = ""

# for i in range(len(string)-1):
#     if string[i] == string[i+1]:
#      count += 1
#     else:
#       string_mini = string_mini + str(count) + string[i]
#       count = 1
# if count > 1 or (string[len(string)-2] != string[-1]):
#     string_mini = string_mini + str(count) + string[-1]

# print(string_mini)


# count1 = ''
# string_max = ''


# for i in range(len(string_mini)):
#     if not string_mini[i].isalpha():
#         count1 += string_mini[i]
#     else:
#         string_max = string_max + string_mini[i] * int(count1)
#         count1 = ''
             

# print(string_max)


