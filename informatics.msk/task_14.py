# n = int(input())
# le = len(str(n))
# n_ = str(n)[::-1]
# s = ''
#
# while le > 0:
#     for i in n_:
#         s += str(int(i) * (2 ** le))
#     le -= 1
# print(s.split('0'))

n = input()
print(int(n,2))