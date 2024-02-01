"""
https://leetcode.com/problems/minimum-falling-path-sum/
"""


class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        row_len = len(matrix[0])
        col_len = len(matrix)
        dp = [matrix[0]] + [[None for _ in range(row_len)] for __ in range(col_len - 1)]
        positions_xy = ((0, -1), (-1, -1), (1, -1))
        for i in range(1, col_len):
            for j in range(0, row_len):
                for x, y in positions_xy:
                    if j + x < 0 or j + x >= row_len:
                        continue
                    current_summ = dp[i + y][j + x] + matrix[i][j]
                    dp[i][j] = min(dp[i][j] or current_summ + 1, current_summ)
        return min(dp[-1])


print(Solution().minFallingPathSum([[-19, 57], [-40, -5]]))
