"""
https://leetcode.com/problems/increasing-triplet-subsequence/
"""


class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        if not nums:
            return False

        min_duplet = None
        current = nums[0]
        for i in range(len(nums)):
            if min_duplet is not None and min_duplet < nums[i]:
                return True
            if current < nums[i]:
                min_duplet = min(min_duplet or nums[i] + 1, nums[i])
            else:
                current = nums[i]
        return False
