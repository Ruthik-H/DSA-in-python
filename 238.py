nums = [1,2,3,4]
a=[]
for i in range(len(nums)):
    b=1
    for j in range(len(nums)):
        if j!=i:
            b*=nums[j]
    a.append(b)
print(a)