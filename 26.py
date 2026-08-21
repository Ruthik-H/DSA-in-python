# # #Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        target=[]
        k=0
        for i in range(len(nums)):
            if nums[i] not in target:
                target.append(nums[i])
                k+=1
        for i in range(k):
            nums[i]=target[i]
        return k 
        return nums
        


        

            


    
