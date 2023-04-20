# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример: 5
#     1 2 3 4 5
#     6
#     -> 5
import random
n = int(input("Введите кол-во чисел: "))
n_list = [random.randint(1, n) for i in range(n)]
print(n_list)
a = int(input("Введите число с которым сравнивать: "))
number = 0
for i in range(len(n_list)):
    if a == n_list[i]:
        number = i
        print(n_list[number])
    elif a + 1 == n_list[i]:
        number = i
        print(n_list[number])
    elif a - 1 == n_list[i]:
        number = i
        print(n_list[number])



