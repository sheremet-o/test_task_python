#  Принимает целое число, а на выходе возвращает то, является ли число простым. Время - 10 минут.
n = int(input())
divs = 0
for i in range(2, n // 2+1):
    if (n % i == 0):
        divs = divs+1
if (divs <= 0):
    print(f'{n} является простым числом.')
else:
    print(f'{n} не является простым числом.')