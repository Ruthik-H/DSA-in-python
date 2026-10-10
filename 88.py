nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
n = 3
m = 3
j=0
for i in range(m,len(nums1)):
    if nums1[i]==0:
        nums1[i]=nums2[j]
        j+=1
    else:
        continue
print(nums1)