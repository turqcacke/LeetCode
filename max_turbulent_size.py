from typing import List


class Solution:

    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if not arr:
            return 0
        if len(arr) == 1:
            return 1

        max_len = 0
        current_max = 0

        def bigger(x, y): return x > y
        def smaller(x, y): return x < y

        f = None
        i = 1

        while i < len(arr):
            k = i - 1
            k_ = i

            if not current_max:
                f = bigger if bigger(arr[k], arr[k_]) else smaller

            if f(arr[k], arr[k_]):
                f = smaller if f == bigger else bigger
                current_max += 1
            else:
                current_max = 0
                if arr[k] == arr[k_]:
                    i += 1
                continue

            i += 1
            max_len = max(max_len, current_max)

        return max_len + 1


print(Solution().maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]))
print(Solution().maxTurbulenceSize([0, 1, 1, 0, 1, 0, 1, 1, 0, 0]))
print(Solution().maxTurbulenceSize([4, 8, 12, 16]))
print(Solution().maxTurbulenceSize([2, 3, 2, 3, 0, 3, 2, 3, 2]))
