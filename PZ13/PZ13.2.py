#2.	В двумерном списке найти среднее арифметическое положительных элементов, кратных 3.
import random

def average_positive_multiples_of_3(matrix):
    multiples_of_3 = []
    for row in matrix:
        for element in row:
            if element > 0 and element % 3 == 0:
                multiples_of_3.append(element)

    if not multiples_of_3:
        return None

    return sum(multiples_of_3) / len(multiples_of_3)
rows = 4
cols = 5
matrix = [[random.randint(-10, 20) for _ in range(cols)] for _ in range(rows)]

print("Матрица:")
for row in matrix:
    print(row)

average = average_positive_multiples_of_3(matrix)

if average is not None:
    print("\nСреднее арифметическое положительных элементов, кратных 3:", average)
else:
    print("\nВ матрице нет положительных элементов, кратных 3.")
