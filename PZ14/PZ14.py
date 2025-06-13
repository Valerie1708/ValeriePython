# . В исходном текстовом файле(hotline1.txt) найти всеномера телефонов,
# соответствующих шаблону 8(000)000-00-00. Посчитать количество полученных
# элементов. После фразы «Горячая линия» добавить фразу «Министерства
# образования Ростовской области», выполнив манипуляции в новом файле.
import re

with open('hotline2.txt', 'r', encoding='utf-8') as file:
    text = file.read()

phone_numbers = re.findall(r'8\(\d{3}\)\d{3}-\d{2}-\d{2}', text)
count = len(phone_numbers)
print(f'Найдено номеров: {count}')

new_text = text.replace('Горячая линия', 'Горячая линия Министерства образования Ростовской области')

with open('hotline2.txt', 'w', encoding='utf-8') as new_file:
    new_file.write(new_text)
