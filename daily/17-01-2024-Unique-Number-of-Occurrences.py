"""
https://leetcode.com/problems/unique-number-of-occurrences
"""


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        occs = {}
        for n in arr:
            occs[n] = occs.get(n, 0) + 1
        return len(occs.keys()) == len(set(occs.values()))
