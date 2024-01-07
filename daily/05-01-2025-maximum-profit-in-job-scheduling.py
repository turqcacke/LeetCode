"""
https://leetcode.com/problems/maximum-profit-in-job-scheduling/
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        ...
"""
from bisect import bisect_right


class SolutionTimeLimit:
    """
    Time Limit Exceed
    """

    def _is_overlapped(self, pair_i: tuple[int, int], pair_j: [int, int], start: list[int], end: list[int]) -> bool:
        earlier = pair_i[-1] if start[pair_i[-1]
                                      ] < start[pair_j[-1]] else pair_j[-1]
        later = pair_j[-1] if earlier == pair_i else pair_i[-1]
        a = (start[earlier], end[earlier])
        b = (start[later], end[later])

        return (a[0] <= b[0]) and (a[1] > b[0])

    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:

        _len = len(startTime)
        dp = profit.copy()

        pairs = [(startTime[i], i) for i in range(_len)]
        pairs.sort()

        for i in range(1, _len):
            for j in range(i):
                index_i = pairs[i][-1]
                index_j = pairs[j][-1]
                if not self._is_overlapped(pairs[i], pairs[j], startTime, endTime):
                    dp[index_i] = max(
                        dp[index_i], profit[index_i] + dp[index_j])
        return max(dp)


class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        jobs = sorted(zip(endTime, startTime, profit))
        jobs.sort()
        dp = [0] * (len(profit) + 1)

        for i, (_, start_time, profit) in enumerate(jobs):
            index_of_closest_finished = bisect_right(
                jobs, start_time, hi=i, key=lambda x: x[0])
            dp[i + 1] = max(dp[i], profit + dp[index_of_closest_finished])
        return dp[-1]


print(Solution().jobScheduling([4, 2, 4, 8, 2],
      [5, 5, 5, 10, 8], [1, 2, 8, 10, 4]))
print(Solution().jobScheduling([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]))
print(Solution().jobScheduling([1, 2, 3, 4, 6],
      [3, 5, 10, 6, 9], [20, 20, 100, 70, 60]))
print(Solution().jobScheduling([1, 1, 1], [2, 3, 4], [5, 6, 4]))
