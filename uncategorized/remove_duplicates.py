from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1 or not nums:
            return nums

        i_1 = 1
        counter = 2
        while i_1 < len(nums):
            i = i_1 - 1
            if nums[i] == nums[i_1] and counter != 2:
                nums.pop(i)
                i += 1
            else:
                i_1 += 1

        return nums


print(Solution().removeDuplicates([1, 1, 1, 2, 2, 3, 3, 4, 4]))
