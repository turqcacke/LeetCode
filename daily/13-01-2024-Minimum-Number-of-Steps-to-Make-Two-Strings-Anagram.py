"""
https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram
"""


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        if len(s) != len(t):
            return 0
        s_set = {}
        c_set = {}
        steps = 0

        for c in s:
            s_set[c] = s_set.get(c, 0) + 1
        for c in t:
            c_set = c_set.get(c, 0) + 1
        for c, count in c_set.items():
            if c in s_set:
                steps += max(count - s_set[c], 0)
            else:
                steps += count
        return steps
