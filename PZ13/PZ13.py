#1.	В двумерном списке элементы второго столбца заменить элементами из одномерного динамического массива соответствующей размерности.
import random

def replace_second_column(matrix, array):
    rows = len(matrix)
    if rows != len(array):
        raise ValueError("Размерность массива не соответствует количеству строк в матрице.")

    for i in range(rows):
        matrix[i][1] = array[i]

rows = 5
cols = 4
matrix = [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]
array = [random.randint(1, 100) for _ in range(rows)]

print("Исходная матрица:")
for row in matrix:
    print(row)

print("\nДинамический массив:")
print(array)
replace_second_column(matrix, array)

print("\nМатрица после замены:")
for row in matrix:
    print(row)
