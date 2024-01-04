from typing import List


class Solution:
    def _is_in_interval(self, x, y, k):
        return x <= k and k <= y

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        overlapping = []
        insert_position = None
        for i in range(len(intervals)):
            cur_interval = intervals[i]
            if insert_position is None and cur_interval[1] > newInterval[0]:
                insert_position = i
            if self._is_in_interval(newInterval[0], newInterval[1], cur_interval[0]) \
                or self._is_in_interval(newInterval[0], newInterval[1], cur_interval[1])\
                    or self._is_in_interval(cur_interval[0], cur_interval[1], newInterval[0])\
            or self._is_in_interval(cur_interval[0], cur_interval[1], newInterval[1]):
                overlapping.append(i)

        if not overlapping and insert_position is None:
            intervals.append(newInterval)
        elif not overlapping:
            intervals.insert(insert_position, newInterval)
        else:
            paste_pos = overlapping[0]
            paste_interval = [min(intervals[overlapping[0]][0], newInterval[0]), max(
                intervals[overlapping[-1]][1], newInterval[-1])]
            intervals = intervals[0:overlapping[0]] + \
                intervals[overlapping[-1] + 1::]
            intervals.insert(paste_pos, paste_interval)

        return intervals
