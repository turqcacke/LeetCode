"""
https://leetcode.com/problems/set-mismatch
"""


class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        s = {i for i in range(1, len(nums) + 1)}
        shadowed = None
        for i in range(len(nums)):
            if nums[i] in s:
                s.remove(nums[i])
                continue
            shadowed = nums[i]
        return [shadowed] + list(s)
