def get_days_in_month(month):
    """
    :param month: Номер месяца (1-12)
    :type month: int
    :return: Количество дней в месяце
    :rtype: int
    :raises ValueError: Если месяц вне диапазона 1-12
    """
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    elif month == 2:
        return 28
    else:
        raise ValueError(f'Недопустимый номер месяца: {month}')
def main():
    try:
        month = int(input('Введите номер месяца (1-12): '))
        days = get_days_in_month(month)
        print(f'В месяце {month} {days} дней.')
    except ValueError as e:
        print(f'Ошибка: {e}')
if __name__ == '__main__':
    main()