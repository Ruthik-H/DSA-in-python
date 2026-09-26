# Count Number of Nice Subarrays
nums = [1,1,2,1,1]
k = 3
ans=0
for i in range(len(nums)):
    for j in range(i,len(nums)):
        w_s=nums[i:j+1]
        count=0
        for x in w_s:
            if x%2!=0:
                count+=1
        if count==k:
            ans+=1
            print(w_s)

print(ans)