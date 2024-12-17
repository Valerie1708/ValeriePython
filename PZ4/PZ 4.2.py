# Дано целое число N (> 1). Найти наибольшее целое число K, при котором
# выполняется неравенство 3K < N.
import math
try:
    N = int(input("Введите целое число N (> 1): "))
    if N <= 1:
        raise ValueError("N должно быть больше 1")
    max_k = int(math.log(N, 3))
    print(f"Наибольшее целое число K, при котором 3^K < N равно {max_k}")
except ValueError as e:
    print(e)

