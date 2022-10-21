def series_sum(n):
    string = ''
    a = 0
    for i in range(n):
        a += 1 / (i * 3 + 1)
    return str(round(a,2))





print(series_sum(1))
print(series_sum(2))
print(series_sum(3))