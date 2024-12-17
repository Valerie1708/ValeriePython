# Ввести 2 числа. Если их произведение отрицательно, умножить его на 8, в противном
# случае увеличить его в 1.5 раза.
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
product = a * b
if product < 0:
    result = product * 8
else:
    result = product * 1.5
print(f"Результат: {result}")
