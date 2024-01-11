# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        left = (root.left, low, high)
        right = (root.right, low, high)
        if root.val < low:
            return self.rangeSumBST(*right)
        if root.val > high:
            return self.rangeSumBST(*left)
        return root.val + self.rangeSumBST(*right) + self.rangeSumBST(*left)


print(Solution())
