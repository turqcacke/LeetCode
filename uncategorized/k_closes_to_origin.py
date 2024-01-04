from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda p: p[1]**2 + p[0]**2, reverse=False)
        return points[:k]


print(Solution().kClosest([[1, 3], [-2, 2]], 1))
print(Solution().kClosest([[3, 3], [5, -1], [-2, 4]], 2))
