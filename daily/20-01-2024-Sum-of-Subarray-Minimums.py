"""
https://leetcode.com/problems/sum-of-subarray-minimums
"""


class Solution:
    _MOD = 10**9 + 7

    def sumSubarrayMins(self, arr: list[int]) -> int:
        s = []
        min_sum = 0
        length = len(arr)
        for i in range(length + 1):
            while s and (i == length or arr[s[-1]] >= arr[i]):
                mid = s.pop()
                left = s[-1] if s else -1
                right = i

                count = (mid - left) * (right - mid) % self._MOD
                min_sum += count * arr[mid] % self._MOD
            s.append(i)
        return min_sum


print(Solution().sumSubarrayMins([11, 81, 94, 43, 3]))
