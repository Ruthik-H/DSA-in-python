#single number
# special problem 

#brute force 
# nums=[2,2,1]
# count=0
# for i in range(len(nums)):
#     count=0
#     for j in range(len(nums)):
#         if(nums[i]==nums[j]):
#             count+=1
#     if count==1:

#         print(nums[i])



# optimal approach 
nums=[2,2,1]
ans=0
for num in nums:
    ans=ans^num
print(ans)



    