# Дан список A размера N и целое число K (1 < K < N). Вывести элементы список с
# порядковыми номерами, кратными K: AK, A2*K, A3*K,... . Условный оператор не
# использовать.
import random
def generate_random_list(size, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(size)]
def extract_elements_by_step(lst, step):
    return lst[step-1::step]
if __name__ == "__main__":
    N = 10  # Размер списка
    K = 3   # Шаг для выбора элементов
    min_value = -100
    max_value = 100
    A = generate_random_list(N, min_value, max_value)
    print("Исходный список:", A)
    result = extract_elements_by_step(A, K)
    print("Элементы с индексами, кратными K:", result)
