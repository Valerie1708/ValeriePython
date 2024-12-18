# Описать функцию Minmax(X, Y), записывающую в переменную X минимальное из
# значений X и Y, а в переменную Y — максимальное из этих значений (X и Y —
# вещественные параметры, являющиеся одновременно входными и выходными).
# Используя четыре вызова этой функции, найти минимальное и максимальное из
# данных чисел A, B, C, D
def minmax(x, y):
    if x < y:
        minimum = x
        maximum = y
    else:
        minimum = y
        maximum = x
    return minimum, maximum
try:
    A = float(input("Введите число A: "))
    B = float(input("Введите число B: "))
    C = float(input("Введите число C: "))
    D = float(input("Введите число D: "))
    min_A, max_B = minmax(A, B)
    min_C, max_D = minmax(C, D)
    min_AC, max_min = minmax(min_A, min_C)
    _, max_ABCD = minmax(max_B, max_D)
    print(f"Минимальное из чисел A, B, C, D: {min_AC}")
    print(f"Максимальное из чисел A, B, C, D: {max_ABCD}")
except ValueError as e:
    print("Ошибка ввода данных! Пожалуйста, введите корректное вещественное число.")
