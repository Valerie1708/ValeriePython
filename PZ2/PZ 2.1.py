while True:
    try:
        A = int(input("Введите число A: "))
        B = int(input("Введите число B: "))
        remains: int = A % B
        print(f"Длина незанятой части отрезка равна {remains}")
    except ValueError:
        print("неверное Значение")