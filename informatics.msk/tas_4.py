a = int(input())
b = int(input())
c = int(input())


summa = (a + b + c)

if summa % 2 == 0:
    print(summa // 2)
else:
    print((summa // 2) + 1)