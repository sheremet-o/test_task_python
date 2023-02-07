# Принимает число (int), а на выходе выдает слово “компьютер” в падеже, соответствующем указанному количеству. Время - 10 минут
computer = int(input())
if computer in [0, 5, 6, 7, 8, 9, 11, 12, 13, 14] or computer % 10 in [0, 5, 6, 7, 8, 9]:
    print(str(computer) + ' компьютеров')
elif computer % 10 == 1:
    print(str(computer) + ' компьютер')
else:
    print(str(computer) + ' компьютера')