k = 0
s = 0

while True:
    n = int(input())
    if n == 0:
        break
    if n != 0:
        s += n
        k += 1

print(s / k)