# with open('forecast.txt') as fin:
#     print(fin.read())

min_t = 1
max_t = 5
k = 2

min_tt = 0
max_tt = 0

while k:
    min_tt =+ (min_t+max_t)//2
    max_tt =+ min_t + max_t
    k -= 1
