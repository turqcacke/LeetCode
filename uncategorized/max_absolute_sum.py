from typing import List


class Solution:

    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_sum = nums[0]
        max_sum = nums[0]

        current_min_s = nums[0]
        current_max_s = nums[0]

        for i in range(1, len(nums)):
            current_max_s = max(nums[i], current_max_s + nums[i])
            current_min_s = min(nums[i], current_min_s + nums[i])

            if current_min_s < min_sum:
                min_sum = current_min_s

            if current_max_s > max_sum:
                max_sum = current_max_s
        return max(abs(min_sum), max_sum)


print(Solution().maxAbsoluteSum([-5, 1, 3, 10]))
print(Solution().maxAbsoluteSum([2, -5, 1, -4, 3, -2]))
print(Solution().maxAbsoluteSum([1, -3, 2, 3, -4]))
