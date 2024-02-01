"""
https://leetcode.com/problems/house-robber
"""


class Solution:
    def rob(self, nums: list[int]) -> int:
        dp = nums.copy()
        for i in range(1, len(nums)):
            prev = 0 if i - 2 < 0 else dp[i - 2]
            dp[i] = max(prev + nums[i], dp[i - 1])
        return dp[-1]


print(Solution().rob([1, 2, 3, 1]))
