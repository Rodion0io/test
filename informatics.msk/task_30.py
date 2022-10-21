n = int(input())
A = [int(i) for i in input().split()]
for i in range(1,len(A)-1):
    A[i] = A[i-1]
print(A)