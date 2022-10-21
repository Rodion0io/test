def range_bit_count(a,b):
    s = 0
    arr = [bin(i)[2:] for i in range(a,b+1)]
    for j in arr:
        s += j.count('1')
    return s



print(range_bit_count(2,7))
print(range_bit_count(0,1))
print(range_bit_count(4,4))