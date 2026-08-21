# sliding window 
#Maximum Average Subarray I
# nums = [1, 12, -5, -6, 50, 3]
# k = 4
# r = 0
# g = k - 1
# max_avg=[]
# while g < len(nums):
#     sum = 0
#     for i in range(r, g + 1):
#         sum = sum + nums[i]
#     avg = sum / k
#     max_avg.append(avg)
#     r += 1
#     g += 1
# print(max(max_avg)) 

#optimal solution

nums = [1, 12, -5, -6, 50, 3]
k = 4
window_sum=sum(nums[0:k])
max_sum=window_sum
for i in range(k,len(nums)):
    window_sum=window_sum-nums[i-k]+nums[i]
    max_sum=max(max_sum,window_sum)

print(max_sum/k)

