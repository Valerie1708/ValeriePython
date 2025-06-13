# 1.В последовательности на n целых элементов в первой ее половине найти
# количество положительных элементов.
def find_positive_num(numbers):
    half_length = len(numbers) // 2
    first_half = numbers[:half_length]
    num_count = len([num for num in first_half if num>=0])
    return num_count


numbers = list(map(int, input('Введите числа через пробел: ').split()))
print(find_positive_num(numbers))