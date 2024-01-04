from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        p = head
        p2 = head.next
        while p != p2 and p2 is not None:
            p = p.next
            p2 = p2.next
            if p2:
                p2 = p2.next
        return p2 is not None
