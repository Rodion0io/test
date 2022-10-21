n = int(input())
A = [int(i) for i in input().split()]
s = 0

for i in A:
    if i > 0:
        s += 1
print(s)