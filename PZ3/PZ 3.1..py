def check_odd_numbers(a, b):
    """
    :param a: Первое целое число
    :type a: int
    :param b: Второе целое число
    :type b: int
    :return: Истина, если ровно одно из чисел нечетное, иначе ложь
    :rtype: bool
    """
    if isinstance(a, int) and isinstance(b, int):
        return (a % 2 != 0) ^ (b % 2 != 0)
    else:
        raise TypeError("Оба значения должны быть целыми числами")

def main():
    try:
        a = int(input("Введите первое целое число: "))
        b = int(input("Введите второе целое число: "))
        if check_odd_numbers(a, b):
            print(f"Истинно, что ровно одно из чисел {a} и {b} нечетное.")
        else:
            print(f"Неверно, что ровно одно из чисел {a} и {b} нечетное.")

    except ValueError as e:
        print(f"Произошла ошибка ввода: {e}. Пожалуйста, введите целые числа.")

if __name__ == "__main__":
    main()
