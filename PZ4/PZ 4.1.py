# Дано целое число N (> 0). Найти сумму N2 + (N + 1)2 + (N + 2)2 + ... + (2N)2
try:
    N = int(input("Введите положительное целое число N: "))
    if N <= 0:
        raise ValueError("Значение N должно быть положительным целым числом.")
    total_sum = 0
    for i in range(N, 2 * N + 1):
        total_sum += i ** 2
    print(f"Сумма квадратов от N^2 до (2N)^2 равна {total_sum}")
except ValueError as e:
    print("Ошибка:", e)

