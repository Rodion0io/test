A = []

count = 0

while True:
    n = int(input())
    if n == 0:
        break
    else:
        A.append(n)

maxi = max(A)

for i in A:
    if i == maxi:
        count += 1
print(count)