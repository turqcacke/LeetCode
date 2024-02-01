"""
https://leetcode.com/problems/daily-temperatures
"""


class Solution:
    def dailyTemperatures(self, temps):
        results = [0] * len(temps)
        stack = []
        for i, e in enumerate(temps):
            while stack and temps[stack[-1]] < e:
                s = stack.pop()
                results[s] = i - s
            stack.append(i)
        return results


cases = [[73, 74, 75, 71, 69, 72, 76, 73]]
for c in cases:
    print(Solution().dailyTemperatures(c))
