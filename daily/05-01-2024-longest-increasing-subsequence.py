"""
https://leetcode.com/problems/longest-increasing-subsequence/?envType=daily-question&envId=2024-01-05
class Solution(object):
    def lengthOfLIS(self, nums):
        ```
        :type nums: List[int]
        :rtype: int
        ```
"""


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0

        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
