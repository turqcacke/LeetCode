"""
https://leetcode.com/problems/longest-common-subsequence
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0

        lower, bigger = (text1, text2) if len(text1) < len(text2) else (text2, text1)

        dp = [[0] * (len(bigger) + 1) for _ in range(len(lower) + 1)]

        for i in range(1, len(lower) + 1):
            for j in range(1, len(bigger) + 1):
                ti = i - 1
                tj = j - 1
                dp[i][j] = (
                    dp[i - 1][j - 1] + 1
                    if lower[ti] == bigger[tj]
                    else max(dp[i - 1][j], dp[i][j - 1])
                )
        return max(dp[-1])


print(Solution().longestCommonSubsequence("abcba", "abcbcba"))
