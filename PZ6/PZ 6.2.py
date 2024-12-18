# Дан список размера N. Найти количество его промежутков монотонности (то есть
# участков, на которых его элементы возрастают или убывают).
import random
def generate_random_list(n, min_value=-10, max_value=10):
    return [random.randint(min_value, max_value) for _ in range(n)]
def count_monotonic_segments(lst):
    try:
        if not lst:
            return 0
        current_length = 1
        direction = None
        monotonic_count = 0
        for i in range(len(lst) - 1):
            if lst[i + 1] > lst[i]:
                new_direction = 'increasing'
            elif lst[i + 1] < lst[i]:
                new_direction = 'decreasing'
            else:
                continue

            if direction is None or direction == new_direction:
                current_length += 1
            else:
                monotonic_count += 1
                current_length = 2
                direction = new_direction
        monotonic_count += 1
        return monotonic_count
    except TypeError as e:
        print(f"Произошла ошибка: {e}. Переданный аргумент должен быть списком чисел.")
        return None
def main():
    N = 10
    lst = generate_random_list(N)
    print("Список:", lst)
    monotonic_count = count_monotonic_segments(lst)
    if monotonic_count is not None:
        print("Количество участков монотонности:", monotonic_count)
    else:
        print("Не удалось посчитать количество участков монотонности.")
if __name__ == "__main__":
    main()
