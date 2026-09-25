nums = [1,0,1,0,1]
goal=2
count=0
for i in range(len(nums)):
    for j in range(i,len(nums)):
        w_s=nums[i:j+1]
        if sum(w_s)==goal:
            count+=1
print(count)

# alternative solution of TC of O(n^2)     
    
# count = 0

# for i in range(len(nums)):
#     current_sum = 0

#     for j in range(i, len(nums)):
#         current_sum += nums[j]

#         if current_sum == goal:
#             count += 1

# print(count)
    