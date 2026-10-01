x = -123
c = list(str(x))
a = 0
b = len(c) - 1
while a < b:
    if c[a] == '-'or c[a]=='+':
        a += 1
    elif c[b] == '-' or c[b]=='+':
        b -= 1
    else:
        c[a], c[b] = c[b], c[a]
        a += 1
        b -= 1
print(int("".join(c)))