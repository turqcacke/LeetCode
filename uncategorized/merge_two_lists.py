from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2

        newl: ListNode = None
        newl_h: ListNode = None

        while l1 is not None and l2 is not None:
            if l1.val > l2.val:
                tmp = l2
                l2 = l2.next
            else:
                tmp = l1
                l1 = l1.next

            if not newl:
                newl = tmp
                newl_h = tmp
                continue
            newl.next = tmp
            newl = newl.next
        else:
            tmp = l1 if l2 is None else l2

        if not newl:
            newl = tmp
            newl_h = newl
        else:
            newl.next = tmp

        return newl_h
