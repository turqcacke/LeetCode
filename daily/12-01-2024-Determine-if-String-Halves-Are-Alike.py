"""
https://leetcode.com/problems/determine-if-string-halves-are-alike
"""


class Solution:
    _VOVEL_SET = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    def halvesAreAlike(self, s: str) -> bool:
        mid = s // 2
        vowel = [0, 0]
        for i in range(mid):
            if s[i] in self._VOVEL_SET:
                vowel[0] += 1
            if s[mid + i] in self._VOVEL_SET:
                vowel[1] += 1
        return vowel[0] == vowel[1]
