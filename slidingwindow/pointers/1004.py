nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

a = 0
max_count = 0

for i in range(len(nums)):
    w_s = nums[a:i + len(nums)]
    a += 1

    remaining_k = k

    for index in range(len(w_s)):
        if w_s[index] == 0 and remaining_k > 0:
            w_s[index] = 1
            remaining_k -= 1

    count = 0
    current = 0

    for m in range(len(w_s)):
        if w_s[m] == 1:
            current += 1
            count = max(count, current)
        else:
            current = 0

    max_count = max(count, max_count)

print(max_count)


# class Solution:
#     def longestOnes(self, nums: list[int], k: int) -> int:
#         left=0
#         max_count=0
#         for right in range(len(nums)):
#             if nums[right]==0:
#                 k-=1
#             while k<0:
#                 if nums[left]==0:
#                     k+=1
#                 left+=1
#             max_count=max(max_count,right-left+1)
#         return max_count