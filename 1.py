#two sum 

#bruteforce technique
# nums = [2,7,11,15]
# target = 9
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i]+nums[j]==target:
#             print(i,j)

# optimal solution 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1={}
        for i in range(len(nums)):
            x=target-nums[i]
            if x in dict1:
                return [dict1[x],i]
            dict1[nums[i]]=i