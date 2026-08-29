# sort colours
nums = [2,0,2,1,1,0]
low=0
high=len(nums)-1
mid=0
while mid<=high:
    if nums[mid]==0:
        nums[low],nums[mid]=nums[mid],nums[low]
        mid+=1
        low+=1
    elif nums[mid]==1:
        mid+=1
    elif nums[mid]==2:
        nums[high],nums[mid]=nums[mid],nums[high]
        high-=1
print(nums)

    