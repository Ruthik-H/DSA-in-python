m = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

top = 0
bottom = len(m) - 1
left = 0
right = len(m[0]) - 1

ans = []

while top <= bottom and left <= right:

    # → Top row
    for i in range(left, right + 1):
        ans.append(m[top][i])
    top += 1

    # ↓ Right column
    if top <= bottom:
        for i in range(top, bottom + 1):
            ans.append(m[i][right])
        right -= 1

    # ← Bottom row
    if left <= right:
        for i in range(right, left - 1, -1):
            ans.append(m[bottom][i])
        bottom -= 1

    # ↑ Left column
    if top <= bottom:
        for i in range(bottom, top - 1, -1):
            ans.append(m[i][left])
        left += 1

print(ans)