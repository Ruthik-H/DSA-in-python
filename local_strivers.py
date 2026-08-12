# To find the second largest number in array 
nums = [1, 2, 4, 5, 6, 7, 2, 10]
largest = nums[0]
second_largest=nums[0]
for num in nums:
    if num > largest:
        second_largest=largest
    
    elif num>second_largest and num!=largest:
            print(second_largest)


