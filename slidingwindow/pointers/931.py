nums = [1,0,1,0,1]
goal=2
count=0
for i in range(len(nums)):
    for j in range(i,len(nums)):
        w_s=nums[i:j+1]
        if sum(w_s)==goal:
            count+=1
print(count)
            
    

    