"""
https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
"""

from __future__ import annotations


class TreeNode:
    def __init__(self, val=0, left: TreeNode = None, right: TreeNode = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: TreeNode | None) -> int:
        def _maxAncestorDiff(
            root: TreeNode | None, mx: int, mn: int, max_diff: int
        ) -> int:
            if not root:
                return max_diff

            max_diff = max(mx - root.val, abs(mn - root.val), max_diff)
            mx = max(root.val, mx)
            mn = min(root.val, mn)

            left_max_diff = _maxAncestorDiff(root.left, mx, mn, max_diff)
            right_max_diff = _maxAncestorDiff(root.right, mx, mn, max_diff)

            return max(left_max_diff, right_max_diff)

        left = (
            None
            if not root.left
            else _maxAncestorDiff(
                root.left,
                root.val,
                root.val,
                max(root.val - root.left.val, abs(root.val - root.left.val)),
            )
        )
        right = (
            None
            if not root.right
            else _maxAncestorDiff(
                root.right,
                root.val,
                root.val,
                max(root.val - root.right.val, abs(root.val - root.right.val)),
            )
        )

        return max(left or right, right or left)
