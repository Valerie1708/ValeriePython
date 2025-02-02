# Дана строка. Вывести строку, содержащую те же символы, но расположенные в
# обратном порядке.
def reverse_string(s):
  return s[::-1]
string_example = "Привет, мир!"
reversed_string = reverse_string(string_example)
print(f"Исходная строка: {string_example}")
print(f"Перевернутая строка: {reversed_string}")
