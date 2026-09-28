nums = [5,2,1,2,5,2,1,2,5]
h={}
left=0
max_sum=0
win_sum=0
for i in range(len(nums)):
    w_S=nums[i] 
    if w_S not in h:
        h[w_S]=1
    else:
        h[w_S]+=1
    win_sum+=nums[i]
    while h[w_S]>1:
        h[nums[left]]-=1
        win_sum-=nums[left]
        left+=1
    if win_sum>max_sum:
        max_sum=win_sum
print(max_sum)
    