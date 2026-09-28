nums = [1, 1, 4, 2, 3]
x = 5
target = sum(nums) - x
left = 0
window_sum = 0
max_len = 0
for right in range(len(nums)):
    window_sum += nums[right]
    while left<=right and window_sum > target:
        window_sum -= nums[left]
        left += 1
    if window_sum == target:
        current_len = right - left + 1
        if current_len > max_len:
            max_len = current_len
if max_len == 0:
    print(-1)
else:
    print(len(nums) - max_len)