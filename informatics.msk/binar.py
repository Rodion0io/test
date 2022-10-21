from random import randint

arr = sorted([randint(1,500) for i in range(200)])

count = 0

le = len(arr) - 1

while count <= le:
    a = (count + le) // 2
    g =