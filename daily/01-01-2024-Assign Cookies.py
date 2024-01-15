"""
https://leetcode.com/problems/assign-cookies
"""


class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        if not g or not s:
            return 0

        g.sort()
        s.sort()

        p1 = 0
        p2 = 0
        n = 0
        while p1 < len(g) and p2 < len(s):
            if g[p1] <= s[p2]:
                n += 1
                p1 += 1
                p2 += 1
            else:
                p2 += 1
        return n


print(Solution().findContentChildren([1, 2, 3], [1, 1]))
