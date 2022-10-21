def f(letter):
    if letter.isupper():
        letter = letter.lower()
    elif letter.islower():
        letter = letter.upper()
    return letter


print(f(input()))