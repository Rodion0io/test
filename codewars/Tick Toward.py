def tick_toward(start, target):
    A = []
    if start[0] == target[0]:
        for i in range(start[1], target[1] + 1):
            A.append((start[0], i))
    if start[0] == target[0] and start[1] > target[1]:
        for i in range(start[1], target[1] - 1, -1):
            A.append(((start[0], i)))
    if start[0] < target[0]:
        for i in range(start[0], target[0] + 1):
            for j in range(start[1], target[1] + 1):
                A.append((,j))
    return A

print(tick_toward((5,5), (5,7)))    #[(5,5), (5,6), (5,7)]
print(tick_toward((3,2), (4,5)))    #[(3,2), (4,3), (4,4), (4,5)]
print(tick_toward((5,1), (5,-2)))   #[(5,1), (5,0), (5,-1), (5,-2)]