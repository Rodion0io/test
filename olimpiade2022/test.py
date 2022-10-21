a = 'ETERNITY'
# r = ''
s=""
for i in range(len(a)):
    j=a.rfind(a[i])+1
    if j-i>len(s):
        s=a[i:j]
print(len(s))
# for i in s:
#     for j in i:
#         if s.find(i,2) == s.rfind(j,0):
#             r += i
# print(r)
