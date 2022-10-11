# # Задача 1. Крестики - нолики.
# # создаем поле

# board = list(range(1,10))

# def draw_board(board):
#    print("-" * 13)
#    for i in range(3):
#       print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#       print("-" * 13)
    
# # draw_board(board)
# # прием ввода пользователя
# def take_input(player_token):
#    valid = False
#    while not valid:
#       player_answer = input("Куда поставим " + player_token+"? ")
#       try:
#          player_answer = int(player_answer)
#       except:
#          print("Некорректный ввод. Вы уверены, что ввели число?")
#          continue
#       if player_answer >= 1 and player_answer <= 9:
#          if(str(board[player_answer-1]) not in "XO"):
#             board[player_answer-1] = player_token
#             valid = True
#          else:
#             print("Эта клетка уже занята!")
#       else:
#         print("Некорректный ввод. Введите число от 1 до 9.")

# # проверяем игровое поле
# def check_win(board):
#    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
#    for each in win_coord:
#        if board[each[0]] == board[each[1]] == board[each[2]]:
#           return board[each[0]]
#    return False
# # выводим игровое поле принимаем воод пользователя и определяем X или 0
# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#            take_input("X")
#         else:
#            take_input("O")
#         counter += 1
#         if counter > 4:
#            tmp = check_win(board)
#            if tmp:
#               print(tmp, "выиграл!")
#               win = True
#               break
#         if counter == 9:
#             print("Ничья!")
#             break
#     draw_board(board)
# main(board)

# input("Нажмите Enter для выхода!")

# # Задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

# # text = 'aaasssddFFsd'
# # # надо получить: 3a3s2d2Fsd

# # lst = [text[i] for i in range(len(text))]
# # print (lst)

# def encode_mess(lst):
#     encode_lst = ""
#     i = 0
#     while (i <= len(lst)-1):
#         count =1
#         ch = lst[i]
#         j=i
#         while (j < len(lst)-1):
#             if (lst[j] == lst[j+1]):
#                 count= count + 1
#                 j = j+1
#             else:
#                 break
#         encode_lst = encode_lst + str(count) + ch
#         i = j+1
        

#     return encode_lst

# text = 'aaasssddFFsd'
# lst = [text[i] for i in range(len(text))]
# print (lst)

# lst1 = encode_mess(lst)
# lst2 = lst1.replace("1", "")
# print(lst2)


# Задача 3. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# # Вариант 1. На двух игроков
# # жеребьевка
# import random
# s = random.randint (1,2)
# print (f'ходит игрок: {s}')

# vsego = 2021
# count = 0
# if (s == 1):
#     while (vsego >0):
#         print ('возьмите не более 28 конфет: ')
#         a = int (input('возьмите не более 28 конфет: '))
#         if (a> 28):
#             print ("возьмите меньше конфет") 
#         else:
#             vsego = vsego - a
#             count = count +1
#             print(vsego)
# print (count)
# if (count % 2 == 0):
#     print ('выиграл игрок 2')
# else:
#     print('выиграл игрок 1')

#  вариант 2.
# Бот, который выиграет всегда, когда ходит первым.
# Первый ход. Надо взять остаток от деления 2021 на 28, чтобы осталось число ходов с целым
# макс. кол-вом конфет за ход.
# import random
# vsego = 202
# max = 28
# count = 0
# с = 0
# a= vsego % max
# print (a)
# print (f'Бот взял {a} конфет')
# vsego = vsego -a
# count = count+1
# while (vsego >0):   
#     # print ('возьмите не более 28 конфет: ')
#     b = int (input ('возьмите не более 28 конфет: '))
#     if (b> 28):
#         print ("возьмите меньше конфет")
#     elif (b == 28):
#         # бот должен разбить 28
#         vsego = vsego - b
#         count = count +1
#         c = random.randint(1,27)
#         # print (c)
#         print (f'Бот взял {c} конфет')
#         vsego = vsego - c
#         count = count +1
#     elif (b < 28):
#         # бот должен дополнить ход игрока до 28
#         vsego = vsego - b
#         count = count +1
#         c = 28 - b
#         print (f'Бот взял {c} конфет')
#         vsego = vsego - c
#         count = count +1

# print (count)
# if (count % 2 == 0):
#     print ('выиграл игрок 2')
# else:
#     print('выиграл игрок 1')        

