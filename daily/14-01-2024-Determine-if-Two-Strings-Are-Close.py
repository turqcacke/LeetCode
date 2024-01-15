"""
https://leetcode.com/problems/determine-if-two-strings-are-close
"""


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        lenght = len(word1)
        w1_set = {}
        w2_set = {}
        for i in range(lenght):
            w1_set[word1[i]] = w1_set.get(word1[i], 0) + 1
            w2_set[word2[i]] = w2_set.get(word2[i], 0) + 1

        d1 = {}
        d2 = {}
        for c, l in w1_set.items():
            if c not in w2_set:
                return False
            if l != w2_set[c]:
                d1[l] = d1.get(l, 0) + 1
                d2[w2_set[c]] = d2.get(w2_set[c], 0) + 1
        return d1 == d2


print(Solution().closeStrings("caaabb", "cbbbaa"))
