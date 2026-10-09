nums = [1,3,4,2,2]
dict1={}
for i in range(len(nums)):
    if nums[i]  in dict1:
        dict1[nums[i]]+=1
    else:
        dict1[nums[i]]=1
# very imp concept like how to get the values from the dictionary
for key,values in dict1.items():
    if values>1:
        print(key)