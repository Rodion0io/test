A = [int(i) for i in input().split(' ')]

B = [j for j in A]

print(*(B[::-1]))