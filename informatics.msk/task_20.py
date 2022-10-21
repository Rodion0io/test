k = 0

# while True:
n = list(map(int,input().split()))
for i in n:
    if i % 2 == 0 and i != 0:
        k += 1
    # if n == 0:
    #     break
    # if n % 2 == 0:
    #     k += 1
print(k)