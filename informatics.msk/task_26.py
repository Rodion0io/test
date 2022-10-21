n = int(input())
A = [int(i) for i in input().split()]

for i in range(len(A)-1):
    if A[i] * A[i+1] > 0:
        print('YES')
        break
else:
    print('NO')