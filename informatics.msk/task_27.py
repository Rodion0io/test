n = int(input())
A = [int(i) for i in input().split()]
s = 0

for i in range(len(A)- 1):
    if A[i] != A[i+1]:
        s += 1
print(s)