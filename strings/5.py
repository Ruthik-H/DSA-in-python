s = "babad"

result = ""

for i in range(len(s)):
    for j in range(i, len(s)):

        substring = s[i:j+1]

        left = 0
        right = len(substring) - 1

        is_palindrome = True

        while left < right:

            if substring[left] != substring[right]:
                is_palindrome = False
                break

            left += 1
            right -= 1

        if is_palindrome and len(substring) > len(result):
            result = substring

print(result)