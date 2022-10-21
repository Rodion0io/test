n = int(input())
A = [int(i) for i in input().split()]
k = int(input())

temp = A[-k:]

for i in range(n-1,0,-1):
    A[i] = A[i-k]

for i in range(k):
    A[i] = temp[i]

print(*A)