def name_that_number(x):
    name_num = {0:'zero', 1:'one', 2:'two', 3:'three',4:'four', 5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',
                20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety'}
    if x < 21:
        return name_num[x]
    else:
        des = (x // 10) * 10
        ed = x % 10
        if ed == 0:
            return name_num[des]
        else:
            return name_num[des] + ' ' + name_num[ed]



print(name_that_number(0))
print(name_that_number(4))
print(name_that_number(9))
print(name_that_number(23))
print(name_that_number(30))


# a = 47
#
# print((a // 10) * 10)