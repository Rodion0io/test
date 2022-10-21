def check(s):
    count = 0
    s = s.split('.')
    if len(s) != 4:
        return False
    for i in s:
        if not i.isdigit() or (len(i) > 1 and i[0] == '0'):
            return False
        if 0 <= int(i) <= 255:
            count += 1
    return count

def is_valid_IP(s):
    if check(s) == 4:
        return True
    else:
        return False


print(is_valid_IP('12.255.56.1'))
print(is_valid_IP(''))
print(is_valid_IP('abc.def.ghi.jkl'))
print(is_valid_IP('127.1.1.0'))
print(is_valid_IP('123.456.789.0'))
print(is_valid_IP('123.045.067.089')) #False