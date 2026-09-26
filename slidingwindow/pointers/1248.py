# # Count Number of Nice Subarrays
# nums = [1,1,2,1,1]
# k = 3
# ans=0
# for i in range(len(nums)):
#     for j in range(i,len(nums)):
#         w_s=nums[i:j+1]
#         count=0
#         for x in w_s:
#             if x%2!=0:
#                 count+=1
#         if count==k:
#             ans+=1
#             print(w_s)

# print(ans)

class Solution:
    def numberOfSubarrays(self, nums, k):
        def atMost(k):
            left = 0
            ans = 0
            for right in range(len(nums)):
                if nums[right] % 2 != 0:
                    k -= 1
                while k < 0:
                    if nums[left] % 2 != 0:
                        k += 1
                    left += 1
                ans += right - left + 1
            return ans
        return atMost(k) - atMost(k - 1)