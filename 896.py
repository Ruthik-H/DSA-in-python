nums = [6,5,4,4]
isincreasing=False
isdecreasing=False
for i in range(1,len(nums)):
    if nums[i]>nums[i-1]:
        isincreasing=True
    elif nums[i]<nums[i-1]:
        isdecreasing=True
if  isdecreasing==True and isincreasing==True:
    print("False")
else:
    print("True")
