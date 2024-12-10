month_number = int(input("Введите номер месяца (1-12): "))

days_in_month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

try:
    days = days_in_month[month_number]
    print(f"В месяце под номером {month_number} {days} дней.")
except KeyError:
    print("Ошибка: Номер месяца должен быть в диапазоне от 1 до 12.")
