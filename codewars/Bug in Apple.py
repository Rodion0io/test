import numpy as np

def sc(apple):
    for i in range(len(apple)):
        for j in range(len(apple)):
            if apple[i][j] == 'B':
                return apple[i][j]





print(sc([
        ["A","A","A","A","A"],
        ["A","B","A","A","A"],
        ["A","A","A","A","A"],
        ["A","A","A","A","A"],
        ["A","A","A","A","A"]
        ]))