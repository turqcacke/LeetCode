class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root.val == p.val or root.val == q.val:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if (left and right) or (right and root.val == min(p.val, q.val)):
            return root

        return left or right


n1 = TreeNode(3)
n2 = TreeNode(1)
n3 = TreeNode(4)
n4 = TreeNode(2)

n1.left = n2
n1.right = n3
n2.right = n4

print(Solution().lowestCommonAncestor(n1, n3, n4))
