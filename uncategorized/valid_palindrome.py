class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(i for i in s if i.isalnum()).lower()

        start_pointer = 0
        end_pointer = 0 if not len(s) else len(s) - 1

        while start_pointer < end_pointer:
            if s[start_pointer] != s[end_pointer]:
                return False

            start_pointer += 1
            end_pointer -= 1

        return True
