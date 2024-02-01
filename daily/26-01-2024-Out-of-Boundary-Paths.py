"""
https://leetcode.com/problems/out-of-boundary-paths
"""


class Solution:
    _MODULO = 1000000000 + 7

    def findPaths(self, m: int, n: int, N: int, startRow: int, startColumn: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1
        paths = ((0, 1), (0, -1), (1, 0), (-1, 0))
        s = 0
        for _ in range(0, N):
            for i in range(m):
                for j in range(n):
                    if i == 0:
                        s += dp[i][j] % self._MODULO
                    if i == m - 1:
                        s += dp[i][j] % self._MODULO
                    if j == 0:
                        s += dp[i][j] % self._MODULO
                    if j == n - 1:
                        s += dp[i][j] % self._MODULO

            dp_c = [i.copy() for i in dp]
            for i in range(m):
                for j in range(n):
                    if dp_c[i][j]:
                        for _i, _j in paths:
                            if (
                                i + _i >= 0
                                and i + _i < m
                                and j + _j >= 0
                                and j + _j < n
                            ):
                                dp[i + _i][j + _j] += dp[i][j] % self._MODULO
                        dp[i][j] = 0

        return s % self._MODULO


print(Solution().findPaths(1, 3, 3, 0, 1))
print(Solution().findPaths(1, 2, 50, 0, 0))
print(Solution().findPaths(2, 2, 2, 0, 0))
