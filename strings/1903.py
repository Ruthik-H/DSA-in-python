# largest odd number in strings
num = "52"

for i in range(len(num) - 1, -1, -1):
    if int(num[i]) % 2 != 0:
        print(num[:i+1])
        break
else:
    print("")