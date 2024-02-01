class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode | None) -> int:
        def _f(
            root: TreeNode | None,
            vals: set,
            level=1,
        ) -> int:
            if not root:
                return 0
            if not root.left and not root.right:
                return 0 if len(vals) > 1 or (len(vals) == 1 and level % 2 != 1) else 1

            if root.val in vals:
                vals.remove(root.val)
            else:
                vals.add(root.val)

            left_count = _f(root.left, vals.copy(), level + 1)
            right_count = _f(root.right, vals.copy(), level + 1)

            return left_count + right_count

        return _f(root, set())


print(Solution().pseudoPalindromicPaths(TreeNode(9)))
