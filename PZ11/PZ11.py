# 1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Минимальный элемент:
# Числа кратные трем:
# Количество чисел кратных трем:

l = ['-99 6 12 -36 20 45 100 -15']
f3 = open('data_3.txt', 'w')
f3.writelines(l)
f3.close()

f4 = open('data_4.txt', 'w', encoding="utf-8")
f4.write('Исходные данные: ')
f4.write('\n')
f4.writelines(l)
f4.close()

f3 = open('data_3.txt')
k = f3.read()
k = k.split()
for i in range(len(k)):
    k[i] = int(k[i])
f3.close()

f3 = open('data_3.txt')
count, min_num, count_digit_3 = 0, 0, 0
digit_3 = []
for i in range(len(k)):
    count += 1
    min_num = min_num if (min_num < k[i]) else k[i]
    if k[i] % 3 == 0:
        digit_3.append(k[i])
        count_digit_3 += 1

f4 = open('data_4.txt', 'a', encoding="utf-8")
f4.write('\n')
print(f'Количество элементов: {count}\nМинимальный элемент: {min_num}\nЧисла кратные трем: {digit_3}\nКоличество чисел кратных трем: {count_digit_3}\n', file=f4)
f4.close()