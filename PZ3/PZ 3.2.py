month_number = int(input("Введите номер месяца (1-12): "))

if month_number in (1, 3, 5, 7, 8, 10, 12):
    days = 31
elif month_number == 2:
    days = 28
else:
    days = 30

print(f"В {month_number}-м месяце {days} дней.")
