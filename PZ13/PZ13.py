# # В двумерном списке найти сумму элементов первых двух строк.
import random
matrix = [[random.randint(-10,10) for _ in range(4)] for _ in range(4)]

print("Исходная матрица:")
for row in matrix:
    print(row)

sum_first_two_rows = sum(map(sum, matrix[:2]))

print("Сумма элементов первых двух строк:", sum_first_two_rows)