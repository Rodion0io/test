def calc(x,a,b):
    s = ''
    x = int(str(x),a)
    while x > 0:
        s += str(x % b)
        x //= b
    return s

x = int(input())
a = 10
b = 2
print(calc(x,a,b))