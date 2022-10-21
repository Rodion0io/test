n = int(input())
A = [int(i) for i in input().split()]

temp = A[-1]
for i in range(n-1,0,-1):
    A[i] = A[i-1]
A[0] = temp
print(*A)