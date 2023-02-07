# Вывод списка через запятую в точкой в конце. Время - 10 минут
list_of_cities = list(map(str, input().strip().split()))
print(", ".join([str(i) for i in list_of_cities]) + '.')
