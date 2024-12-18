# Составить функцию решения задачи: из заданного числа вычли сумму его цифр. Из
# результата вновь вычли сумму его цифр и т. д. Через сколько таких действий
# получится нуль?
def foo(n):
    steps = 0
    while n != 0:
        digits_sum = sum(int(digit) for digit in str(n))
        n -= digits_sum
        steps += 1
    return steps
try:
    number = int(input("Введите число: "))
    steps = foo(number)
    print(f"Через {steps} шагов получится ноль.")
except ValueError as e:
    print("Ошибка ввода данных! Пожалуйста, введите корректное целое число.")
