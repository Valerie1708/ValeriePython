# Дан список размера N. Осуществить сдвиг элементов список вправо на одну
# позицию (при этом A1 перейдет в A2, A2 — в A3, ..., AN-1 — в AN, a исходное значение
# последнего элемента будет потеряно). Первый элемент полученного списка
# положить равным 0.
import random
def generate_random_list(size, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(size)]
def shift_right_and_set_first_to_zero(lst):
    shifted_lst = lst[1:] + [0]  # Копируем все элементы кроме первого и добавляем ноль в конец
    shifted_lst[0] = 0           # Устанавливаем первый элемент равным нулю
    return shifted_lst
if __name__ == "__main__":
    N = 10  # Размер списка
    min_value = -100
    max_value = 100
    original_list = generate_random_list(N, min_value, max_value)
    print("Исходный список:", original_list)
    shifted_list = shift_right_and_set_first_to_zero(original_list)
    print("Результат сдвига:", shifted_list)
