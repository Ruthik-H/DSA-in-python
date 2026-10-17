
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        freq = {0: 1}
        for num in nums:
            prefix_sum += num
            need = prefix_sum - k
            count += freq.get(need, 0)
            freq[prefix_sum] = freq.get(prefix_sum, 0) + 1
        return count
