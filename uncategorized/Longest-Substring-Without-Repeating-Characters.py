class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0

        s_set: set = set()
        max_s = len(s_set)

        while right < len(s):
            if len(s_set) > max_s:
                max_s = len(s_set)

            if s[right] not in s_set:
                s_set.add(s[right])
                right += 1
            else:
                s_set.remove(s[left])
                left += 1
        return max(max_s, len(s_set))
