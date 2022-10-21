n = int(input())
A = [int(i) for i in input().split()]
count = 0

for i in range(1,len(A)-1):
    if A[i-1] < A[i] > A[i+1]:
        count += 1
print(count)
    # print(A[i],A[i+1],A[i-1])