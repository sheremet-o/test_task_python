#  На вход принимает число, а на выходе получает число, округленное до пятерок. Время - 30 мин.
i = float(input())
rounded_i = int(i + (0.5 if i > 0 else -0.5))
if rounded_i % 10 in [1, 2]:
    print(rounded_i - int(rounded_i % 10))
elif rounded_i % 10 in [8, 9]:
    print(rounded_i - int(rounded_i % 10) + 10)
elif rounded_i % 10 in [3, 4, 6, 7]:
    print(rounded_i - int(rounded_i % 10) + 5)
else: 
    print(rounded_i)
