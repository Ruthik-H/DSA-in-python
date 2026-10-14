nums = [2,3,1,2,4,3]
target = 7
min_len=float('inf')
a=0
w_sum=0
for i in range(len(nums)):
    w_sum+=nums[i]
    while w_sum>=target:
        min_len=min(min_len,i-a+1)
        w_sum-=nums[a]
        a+=1
if min_len==float('inf'):
    print(0)
else:
    print(min_len)
   


            

