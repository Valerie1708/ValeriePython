# Дан номер месяца — целое число в диапазоне 1-12 (1 — январь, 2 — февраль и т. д.).
# Определить количество дней в этом месяце для невисокосного года.
try:
    month_number = int(input("Введите номер месяца (1-12): "))
    if not 1 <= month_number <= 12:
        raise ValueError("Номер месяца должен быть в диапазоне от 1 до 12")
    if month_number in (1, 3, 5, 7, 8, 10, 12):
        days = 31
    elif month_number == 2:
        days = 28
    else:
        days = 30
    print(f"В {month_number}-м месяце {days} дней.")
except ValueError as e:
    print("Ошибка:", e)

