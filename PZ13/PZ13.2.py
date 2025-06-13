# В двумерном списке найти минимальный и максимальные элементы.
import random
matrix = [[random.randint(-10,10) for _ in range(4)] for _ in range(4)]

print("Исходная матрица:")
for row in matrix:
    print(row)

min_num = min((min(_) for _ in matrix))
print('Минимальное число: ', min_num)

max_num = max((max(_) for _ in matrix))
print('Максимальное число: ', max_num)