nums = [4, 3, 1, 6]
for i in range(len(nums) - 1):
    if nums[i] % 2 == nums[i + 1] % 2:
        print(False)
        break
else:
    print(True)