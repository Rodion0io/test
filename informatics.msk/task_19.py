x = int(input())
p = int(input())
y = int(input())
years = 0

while x < y:
    x += x * (p / x)
    years += 1
print(years)