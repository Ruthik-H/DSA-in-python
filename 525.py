nums = [0,1,1,1,1,1,0,0,0]
n=len(nums)
max_len=0
for a in range(n):
    count1=0
    count2=0
    for b in range(a,n):
        if nums[b]==1:
            count1+=1
        else:
            count2+=1
        if count1==count2:
            max_len=max(max_len,b-a+1)
print(max_len)

