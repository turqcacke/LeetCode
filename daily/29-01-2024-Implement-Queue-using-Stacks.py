"""
https://leetcode.com/problems/implement-queue-using-stacks
"""


class MyQueue:
    def __init__(self):
        self.s = list()
        self.queue = list()

    def push(self, x: int) -> None:
        while self.queue:
            self.s.append(self.queue.pop())

        self.s.append(x)

        while self.s:
            self.queue.append(self.s.pop())

    def pop(self) -> int:
        return self.queue.pop()

    def peek(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return not len(self.queue)


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(12)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
