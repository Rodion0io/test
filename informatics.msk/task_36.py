n = int(input())
A = [int(i) for i in input().split(' ')]

mini = min(A)
maxi = max(A)


for i in range(n):
    maxi[i] = mini[i]
    mini[i] = maxi[i]

print(A)