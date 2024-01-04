class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_map = {}

        for i in magazine:
            if i not in mag_map:
                mag_map[i] = 1
                continue
            mag_map[i] += 1

        for i in ransomNote:
            if i not in mag_map:
                return False

            mag_map[i] -= 1
            if mag_map[i] < 0:
                return False
        return True
