# Дан словарь с произвольным количеством элементов. Выяснить
# имеется ли в нем элемент с ключом «фрукт = яблоко» и если он отсутствует, то
# добавить его в словарь. Вывести на экран первоначальный словарь и измененный.
def check_and_add_apple(my_dict):

    original_dict = my_dict.copy()

    if "фрукт = яблоко" not in my_dict:
        my_dict["фрукт = яблоко"] = True

    return original_dict, my_dict
my_dictionary1 = {"овощ": "морковь", "напиток": "чай"}
original, modified = check_and_add_apple(my_dictionary1)
print("Исходный словарь:", original)
print("Измененный словарь:", modified)

my_dictionary2 = {"фрукт = яблоко": False, "цвет": "синий"}
original, modified = check_and_add_apple(my_dictionary2)
print("\nИсходный словарь:", original)
print("Измененный словарь:", modified)
