def task_2(string):
    se = set(string)
    s = ''
    if len(string) == len(se):
        return 1
    else:
        for i in range(len(string)):
            j = string.rfind(string[i]) + 1
            if j - i > len(s):
                s = string[i:j]
        return len(s)






print(task_2(input()))
# print(task_2(input()))

#ETERNITY