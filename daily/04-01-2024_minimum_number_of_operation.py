"""
https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/
class Solution(object):
    def minOperations(self, nums):
        ```
        :type nums: List[int]
        :rtype: int
        ```
"""


class Solution(object):
    def __min_operations(self, n: int) -> int:
        actions = 0
        while n % 3 != 0 and n > 0:
            actions += 1
            n = n - 2
        return actions + (n // 3) if n >= 0 else n

    def minOperations(self, nums: list[int]):
        nums_dict = {}
        operations = 0

        for n in nums:
            nums_dict[n] = nums_dict.get(n, 0) + 1

        for _, count in nums_dict.items():
            min_operations = self.__min_operations(count)
            if min_operations == -1:
                return -1
            operations += min_operations
        return operations


print(Solution().minOperations([2, 3, 3, 2, 2, 4, 2, 3, 4]))
print(Solution().minOperations([1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
      1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2]))
print(Solution().minOperations([1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
      1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2]))
print(Solution().minOperations([2, 1, 2, 2, 3, 3]))
