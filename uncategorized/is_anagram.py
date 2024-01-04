from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        target_pos = len(nums) // 2 - 1 if len(nums) > 1 else 0

        left = 0
        right = len(nums)

        while left < right:
            if nums[target_pos] == target:
                return target_pos
            elif nums[target_pos] > target:
                right = target_pos - 1
            else:
                left = target_pos + 1
            target_pos = (left + right) // 2
        return -1 if target_pos >= len(nums) or nums[target_pos] != target else target_pos


print(Solution().search([-1, 0, 3, 5, 9, 12], 13))
