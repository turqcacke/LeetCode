"""
https://leetcode.com/problems/evaluate-reverse-polish-notation
"""


class Solution:
    _actions = {
        "*": int.__mul__,
        "+": int.__add__,
        "-": int.__sub__,
        "/": lambda x, y: int(int.__truediv__(x, y)),
    }

    def evalRPN(self, tokens: list[str]) -> int:
        if len(tokens) == 1:
            return tokens[-1]
        unused_nums = list()

        for i in range(0, len(tokens)):
            token = tokens[i]

            if token not in self._actions:
                unused_nums.append(int(token))
                continue

            s, f = unused_nums.pop(), unused_nums.pop()
            unused_nums.append(self._actions.get(token)(f, s))

        return unused_nums[-1]


cases = [
    ["2", "1", "+", "3", "*"],
    ["4", "13", "5", "/", "+"],
    ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],
    ["18"],
    ["4", "-2", "/", "2", "-3", "-", "-"],
]

for case in cases:
    print(Solution().evalRPN(case))
