n = int(input())

if n % 2 == 0:
    print(2 * 3**(n//2))
elif n % 2 != 0:
    print(4 * 3**(n//2))