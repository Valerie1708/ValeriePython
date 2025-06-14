# В исходном текстовом файле(Dostoevsky.txt) найти все варианты фамилии
#Достоевского (т.е. с различными окончаниями, например, Достоевский,
#Достоевского) в единственном экземпляре.
import re
def find_dostoevsky_variants(filename="Dostoevsky.txt"):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
        pattern = r"[Дд]остоевск(?:ий|ого|ому|им|ом|ая|ое|ие|их|ам|а|у)"
        matches = re.findall(pattern, text)
        return set(matches)

    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден.")
        return set()
    except Exception as e:
        print(f"Ошибка при обработке файла: {e}")
        return set()
if __name__ == '__main__':
    variants = find_dostoevsky_variants()

    if variants:
        print("Найденные варианты фамилии Достоевского:")
        for variant in variants:
            print(variant)
    else:
        print("Варианты фамилии Достоевского не найдены.")
