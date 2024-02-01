"""
https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions
"""

from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        l = []
        while nums:
            s = set()
            i = 0
            while i < len(nums):
                if nums[i] in s:
                    i += 1
                    continue
                s.add(nums[i])
                del nums[i]
            l.append(list(s))
        return l
