class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        nums.sort()
        r = []
        sub_arr = []
        c = None
        for e in nums:
            if c is None:
                c = e

            if abs(c - e) <= k:
                sub_arr.append(e)
            else:
                c = e
                if len(sub_arr) < 3:
                    return []
                sub_arr = []

            if len(sub_arr) >= 3:
                c = None
                r.append(sub_arr)
                sub_arr = []
        return r


cases = [[[1, 3, 4, 8, 7, 9, 3, 5, 1], 2], [[1, 3, 3, 2, 7, 3], 3]]
for c in cases:
    print(Solution().divideArray(*c))
