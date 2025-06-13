# 2.Из заданной строки отобразить только символы нижнего регистра.
# Использовать библиотеку string. Строка'In PyCharm, you can specify third-party standalone applications and run them as External Tools'

from string import ascii_lowercase

string_new = 'In PyCharm, you can specify third-party standalone applications and run them as External Tools'
str_1 = [i for i in string_new if i in ascii_lowercase]
print(str_1)