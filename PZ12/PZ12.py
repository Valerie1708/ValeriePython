#1.Даны 	две 	последовательности.
# Найти 	элементы, 	общие 	для 	двух последовательностей и их количество.
def find_common_elements(seq1, seq2):
    set1 = set(seq1)
    set2 = set(seq2)
    common_elements = list(set1.intersection(set2))
    return common_elements, len(common_elements)
sequence1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sequence2 = [5, 7, 9, 11, 13, 15, 1, 1]

common, count = find_common_elements(sequence1, sequence2)

print("Общие элементы:", common)
print("Количество общих элементов:", count)
