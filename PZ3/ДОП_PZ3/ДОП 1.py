# Ввод двух чисел
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
product = a * b
if product < 0:
    result = product * 8
else:
    result = product * 1.5
print(f"Результат: {result}")
