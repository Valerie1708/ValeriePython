#  Ввести 4 числа. Найти и вывести на экран сумму и количество отрицательных
# чисел.
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
d = int(input("Введите четвертое число: "))
negative_count = sum([x < 0 for x in [a+b+c+d]])
print(f"Сумма чисел: {sum}")
print(f"Количество отрицательных чисел: {negative_count}")
