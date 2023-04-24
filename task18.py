# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример: 5
#     1 2 3 4 5
#     6
#     -> 5
# import random
# n = int(input("Введите кол-во чисел: "))
# n_list = [random.randint(1, n) for i in range(n)]
n_list = [1, 3, 9]
print(n_list)
a = int(input("Введите число с которым сравнивать: "))
# number = 0
# for i in range(len(n_list)):
#     if a == n_list[i]:
#         number = i
#         print(n_list[number])
#     elif a + 1 == n_list[i]:
#         number = i
#         print(n_list[number])
#     elif a - 1 == n_list[i]:
#         number = i
#         print(n_list[number])

count = 1
finish = False
while not finish:
    if a in n_list:
        print('ближайшее:', a)
        finish = True
    elif a - count in n_list and a + count in n_list:
        print('ближайшие:', a - count, 'и', a + count)
        finish = True
    elif a - count in n_list:
        print('ближайшее:', a - count)
        finish = True
    elif a + count in n_list:
        print('ближайшее:', a + count)
        finish = True
    count += 1
