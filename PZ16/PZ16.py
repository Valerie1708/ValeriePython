#1.	Создайте класс "Калькулятор" с методами "сложение", "вычитание",
# "умножение" и "деление". Каждый метод должен принимать два аргумента и возвращать результат операции.
class Calculator:
    def addition(self, x, y):
        return x + y

    def subtraction(self, x, y):
        return x - y

    def multiplication(self, x, y):
        return x * y

    def division(self, x, y):

        Returns:
            Результат деления двух чисел.
calculator = Calculator()

result_addition = calculator.addition(5, 3)
print(f"5 + 3 = {result_addition}")

result_subtraction = calculator.subtraction(10, 4)
print(f"10 - 4 = {result_subtraction}")

result_multiplication = calculator.multiplication(6, 7)
print(f"6 * 7 = {result_multiplication}")

try:
    result_division = calculator.division(20, 5)
    print(f"20 / 5 = {result_division}")

    result_division_by_zero = calculator.division(10, 0)
    print(f"10 / 0 = {result_division_by_zero}")
except ValueError as e:
    print(f"Ошибка: {e}")
