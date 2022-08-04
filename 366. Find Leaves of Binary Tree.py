from collections import defaultdict
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:

        levels = defaultdict(list)

        def node_number(node):
            if not node:
                return -1
            number = max(node_number(node.left), node_number(node.right)) + 1
            levels[number].append(node.val)
            return number

        node_number(root)

        return levels.values()
