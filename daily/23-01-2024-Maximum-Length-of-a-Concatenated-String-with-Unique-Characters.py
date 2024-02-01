"""
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters
"""


class Solution:
    def maxLength(self, arr: list[str]) -> int:
        def _f(arr: list[str], back_track_arr: list[str]):
            if not arr:
                if not back_track_arr:
                    return 0
                return len(max(back_track_arr, key=lambda x: len(x)))

            for i in back_track_arr:
                e = arr[0]
                s = e + i
                if len(set(s)) < len(s):
                    continue
                back_track_arr.append(s)

            _m = _f(arr[1::], back_track_arr)

            return _m

        _m = 0
        for i in range(len(arr)):
            a = [] if len(set(arr[i])) < len(arr[i]) else [arr[i]]
            _m = max(
                _m,
                _f(arr[i + 1 : :], a),
            )
        return _m


print(Solution().maxLength(["abc", "ax", "dlmn", "dy"]))
