nums = [-2147483648,0,2147483647]
k =100000
k=k%len(nums)
a1=nums[len(nums)-k:]
a2=nums[0:len(nums)-k]
a3=a1+a2
nums=a3
print(nums)






