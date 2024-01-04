from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0

            left_depth = depth(root.left)
            right_depth = depth(root.right)

            if abs(left_depth - right_depth) > 1 or left_depth == -1 or right_depth == -1:
                return -1
            return max(left_depth, right_depth) + 1
        return depth(root) != -1