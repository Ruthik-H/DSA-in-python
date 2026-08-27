nums = [3, 1, -2, -5, 2, -4]
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[j] < 0:
            temp = nums[i + 1]
            nums[i + 1] = nums[j]
            nums[j] = temp
            break
print(nums)


# for optimal 
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)

        positive = 0
        negative = 1

        for num in nums:
            if num > 0:
                result[positive] = num
                positive += 2
            else:
                result[negative] = num
                negative += 2

        return result


