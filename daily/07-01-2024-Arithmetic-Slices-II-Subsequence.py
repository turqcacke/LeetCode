"""
https://leetcode.com/problems/arithmetic-slices-ii-subsequence
"""
from collections import defaultdict


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        total_count = 0
        dp: list[dict] = [{} for _ in nums]

        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                # Used for sequentional similar values
                dp[i][diff] = 1 + dp[i].get(diff, 0)
                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    total_count += dp[j][diff]
        return total_count


print(Solution().numberOfArithmeticSlices([7, 7, 7, 7, 7]))
print(Solution().numberOfArithmeticSlices([2, 4, 6, 8, 10]))
