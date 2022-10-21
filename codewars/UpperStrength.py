def alex_mistakes(number_of_katas, time_limit):
    mistake = 0
    push = 5
    normal_time = number_of_katas * 6
    if (6 * number_of_katas) == time_limit:
        return 0
    while time_limit > normal_time:




print(alex_mistakes(10,120))
print(alex_mistakes(11,120))
print(alex_mistakes(3,45))
print(alex_mistakes(8,120))
print(alex_mistakes(6,60))
print(alex_mistakes(9,180))
print(alex_mistakes(20,120))
print(alex_mistakes(20,125))
print(alex_mistakes(20,130))
print(alex_mistakes(20,135))