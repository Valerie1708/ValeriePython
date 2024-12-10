# Четное или нечетное число
number = int(input("Введите число: "))
if number % 2 == 0:
    result = number / 4
else:
    result = number * 5
print(f"Результат: {result}")
