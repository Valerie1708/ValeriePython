# Ввод двухзначного числа
num = int(input("Введите двухзначное число: "))
digit1 = num // 10
digit2 = num % 10
sum_digits = digit1 + digit2
if sum_digits % 2 == 0:
    result = num + 2
else:
    result = num - 2
print(f"Результат: {result}")
