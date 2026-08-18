#two sum 

#bruteforce technique
# nums = [2,7,11,15]
# target = 9
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i]+nums[j]==target:
#             print(i,j)

# optimal solution 
nums = [2,7,11,15]
target = 9
for i in range(len(nums)):
    x=target-nums[i]
    if x in nums:
        if nums.index(x) > i:
            print(i,nums.index(x))
        