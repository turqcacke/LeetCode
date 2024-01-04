class Solution:
    def isValid(self, s: str) -> bool:
        copy = ""
        while s and copy != s:
            copy = s
            s = s.replace('()', '').replace('{}', '').replace('[]', '')
        return not s
