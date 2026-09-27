nums = [3,5,6,7]
target = 9
count=0
a=0
b=len(nums)-1
while a<=b:
    if nums[a]+nums[b]<=target:
        MOD = 10**9 + 7
        count+=2**(b-a)
        count%=MOD
        a+=1
    else:
        b-=1
print(count)

