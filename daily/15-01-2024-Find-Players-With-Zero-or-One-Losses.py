"""
https://leetcode.com/problems/find-players-with-zero-or-one-losses
"""
from typing import List
from bisect import bisect_right
from functools import cmp_to_key


class Solution:
    def findWinners1(self, matches: List[List[int]]) -> List[List[int]]:
        suitable: dict[int, int] = {}
        losers = set()

        for winner, loser in matches:
            if winner not in losers:
                suitable[winner] = suitable.get(winner, 0)
            if loser not in losers:
                suitable[loser] = suitable.get(loser, 0) + 1
                if suitable[loser] > 1:
                    suitable.pop(loser)
                    losers.add(loser)

        r = list(suitable.keys())
        r = sorted(
            r, key=cmp_to_key(lambda x, y: (suitable[x] - suitable[y]) or (x - y))
        )
        one_starting = bisect_right(r, 0, key=lambda x: suitable[x])
        return [r[:one_starting], r[one_starting:]]

    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        zeros = set()
        ones = set()
        losers = set()

        for winner, loser in matches:
            if winner not in losers and winner not in ones:
                zeros.add(winner)
            if loser not in losers:
                if loser in ones:
                    ones.remove(loser)
                    losers.add(loser)
                else:
                    if loser in zeros:
                        zeros.remove(loser)
                    ones.add(loser)
        z = list(zeros)
        o = list(ones)
        z.sort()
        o.sort()
        return [z, o]


print(
    Solution().findWinners(
        [
            [1, 3],
            [2, 3],
            [3, 6],
            [5, 6],
            [5, 7],
            [4, 5],
            [4, 8],
            [4, 9],
            [10, 4],
            [10, 9],
        ]
    )
)
