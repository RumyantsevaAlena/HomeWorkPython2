# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
# 5 -> 1 0 1 1 0
# 2
import random
n_coin = int(input("Введите кол-во монет: "))
facets = []
for i in range(n_coin):
    facet = random.randint(0, 1)
    facets.append(facet)
print(facets)
max_long = 0
curr_long = 0
for facet in facets:
    if facet == 0:
        curr_long += 1
    else:
        if curr_long > max_long:
            max_long = curr_long
            curr_long = 0
print(max_long)
