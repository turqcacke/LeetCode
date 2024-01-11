"""
https://leetcode.com/problems/leaf-similar-trees
"""

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __end_node(self, root: Optional[TreeNode], store: list) -> set:
        if not root:
            return store

        if not root.left and not root.right:
            store.append(root.val)
            return store

        self.__end_node(root.left, store)
        self.__end_node(root.right, store)
        return store

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        left_set = self.__end_node(root1, list())
        right_set = self.__end_node(root2, list())
        if len(left_set) != len(right_set):
            return False
        print(right_set)
        print(left_set)
        for i in range(len(left_set)):
            if left_set[i] != right_set[i]:
                return False
        return True
