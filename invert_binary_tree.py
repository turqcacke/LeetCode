from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue: List[TreeNode] = []

        if root:
            queue.append(root)

        while len(queue) > 0:
            element = queue.pop()

            tmp = element.right
            element.right = element.left
            element.left = tmp

            if element.left:
                queue.append(element.left)
            if element.right:
                queue.append(element.right)

        return root
