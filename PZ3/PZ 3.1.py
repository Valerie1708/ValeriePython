# Даны два целых числа: A, B. Проверить истинность высказывания: «Ровно одно из
# чисел A и B нечетное».
try:
    A = int(input("Введите первое целое число: "))
    B = int(input("Введите второе целое число: "))

    # Проверяем, является ли сумма двух чисел нечётной
    if (A + B) % 2 == 1:
        print(f"Ровно одно из чисел {A} и {B} нечетное.")
    else:
        print(f"Не выполнено условие: ровно одно из чисел {A} и {B} должно быть нечетным.")

except ValueError as e:
    print("Ошибка ввода данных! Пожалуйста, введите корректное целое число.")
