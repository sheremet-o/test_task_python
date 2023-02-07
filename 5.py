#   Метод, который определяет, какие элементы присутствуют в двух экземплярах в каждом из массивов. Время - 15 минут.

result = []

list_one = list(map(int, input().strip().split()))
list_two = list(map(int, input().strip().split()))

duplicates_one = {i for i in list_one if list_one.count(i) > 1}
duplicates_two = {i for i in list_two if list_two.count(i) > 1}

all_elements = set(list_one + list_two)

for el in all_elements:
    if el in duplicates_one and el in duplicates_two:
        result.append(el)

print(result)
