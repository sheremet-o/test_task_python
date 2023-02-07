# Метод, который в консоль выводит таблицу умножения. Вермя - 10 минут.
n = int(input())

for i in range(1, n + 1):
    for j in range(i, i * n + 1, i):
        print(j, end='\t')
    print()