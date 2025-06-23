# 2. Из предложенного текстового файла (new18-20.txt) вывести на экран его содержимое,
# количество символов в тексте. Сформировать новый файл, в который поместить строку
# наибольшей длины.
d = 0
max_line = ""
len_max = 0
f1 = open('new18-20.txt', encoding='utf-8')
for i in f1:
    print(i, end='')
    if len(i) > len(max_line):
        max_line = i
        len_max = len(i)
    for j in i:
        d += 1
print(end='\n')
print('Количество символов в тексте: ', d, end='\n')
new_file = open('new18-20.txt', 'w', encoding='utf-8')
print(f"Cтрока наибольшей длины:\n{max_line}", file=new_file)
print(f"Длина строки:\n{len_max}", file=new_file)