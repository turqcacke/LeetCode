"""
https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class NodeWithParent(TreeNode):
    def __init__(self, parent=None, *args, **kwargs):
        self.parent = parent
        super().__init__(*args, **kwargs)


class Solution:
    def _build_graph(self, root: Optional[TreeNode], start: int) -> NodeWithParent:
        def dfs_tree(root: Optional[TreeNode], side: int = 0, parent_node: Optional[NodeWithParent] = None):
            if not root:
                return None
            current_node = NodeWithParent(
                val=root.val, parent=parent_node)
            if parent_node:
                if side == 1:
                    parent_node.left = current_node
                if side == 2:
                    parent_node.right = current_node

            start_node_left = dfs_tree(root.left, 1, current_node)
            start_node_right = dfs_tree(root.right, 2, current_node)

            if current_node.val == start:
                return current_node

            return start_node_left or start_node_right
        return dfs_tree(root)

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph_start = self._build_graph(root, start)
        step = 0
        queue: list[list[NodeWithParent]] = [[graph_start]]
        infested_nodes = {graph_start}
        while queue:
            level_nodes = queue.pop()
            next_level_nodes = []
            for node in level_nodes:
                infested_nodes.add(node)
                if node.left and node.left not in infested_nodes:
                    next_level_nodes.append(node.left)
                if node.right and node.right not in infested_nodes:
                    next_level_nodes.append(node.right)
                if node.parent and node.parent not in infested_nodes:
                    next_level_nodes.append(node.parent)
            if next_level_nodes:
                queue.append(next_level_nodes)
                step += 1
        return step


print(Solution().amountOfTime(TreeNode(1, TreeNode(2), TreeNode(3)), 2))
