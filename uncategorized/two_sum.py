from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}
        for i in range(len(nums)):
            k = target - nums[i]
            if nums[i] in checked:
                return [checked[nums[i]], i]
            checked[k] = i
        return []
