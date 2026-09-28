# sliding window 
nums = [1,1,4,2,3]
x = 5
b=sum(nums)
a=b-x
max_len=0
left=0
w_s=0
for right in range(len(nums)):
        w_s+=nums[right]
        while w_s>a:
             w_s-=nums[left]
             left+=1
        if (w_s)==a and (w_s)>max_len:
            max_len=(w_s)
if max_len==0:
    print("-1")
else:
    removed_elements=len(nums)-max_len
    print(removed_elements)

        
