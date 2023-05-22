# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод:           Вывод:3 3 2 12
# 7 
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)

def nums_list(n):
    result_list = []
    for i in range(n):
        result_list.append(int(input('Введите элемент: ')))
    return result_list


# print(nums_list(7))

def new_list():
    list_1 = input("Введите эл-ты массива через пробел: ").split()
    for k in range(len(list_1)):
        list_1[k] = int(list_1[k])
    return list_1


def dif_list(*args):
    list_a, list_b, *x = args
    list_c = []
    for i in list_a:
        if i not in list_b:
            list_c.append(i)
    return list_c


list_1 = [3, 1, 3, 4, 2, 4, 12]
list_2 = [4, 15, 43, 1, 15, 1]
print(dif_list(list_1, list_2))


