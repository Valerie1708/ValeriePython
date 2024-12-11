A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
is_A_odd = A % 2 != 0
is_B_odd = B % 2 != 0
if is_A_odd != is_B_odd:
    print("Истинно, что ровно одно из чисел A и B нечетное.")
else:
    print("Неверно, что ровно одно из чисел A и B нечетное.")
