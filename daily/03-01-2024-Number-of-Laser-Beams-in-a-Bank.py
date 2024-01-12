"""
https://leetcode.com/problems/number-of-laser-beams-in-a-bank
"""


class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        prev_beams_count = [0] * len(bank)
        prev_beams_count[0] = bank[0].count("1")
        beams_count = 0
        for row_i in range(1, len(bank)):
            beams = bank[row_i].count("1")
            prev_beams_count[row_i] = beams if beams else prev_beams_count[row_i - 1]
            beams_count += prev_beams_count[row_i - 1] * beams
        return beams_count


print(Solution().numberOfBeams(["011001", "000000", "010100", "001000"]))
