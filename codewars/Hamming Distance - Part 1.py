def hamming_distance(a, b):
    difference = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] != b[j]:
                difference += 1
    return difference


print(hamming_distance('100101','101001'))