a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a % 2 == c % 2 and b % 2 == d % 2:
    print('NO')
elif a % 2 != c % 2 and b % 2 != d % 2:
    print('NO')
else:
    print('YES')


