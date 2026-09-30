arr = [1, 2, 3, 4, 5]

k = 4
x = 3

a = 0
b = len(arr) - 1

remove = len(arr) - k

while remove > 0:

    left = abs(x - arr[a])
    right = abs(x - arr[b])

    if left <= right:
        b -= 1
    else:
        a += 1

    remove -= 1

print(arr[a:b+1])