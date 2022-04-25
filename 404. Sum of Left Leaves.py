# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        result = 0
        stack = [(root, 'r')]
        while stack:
            node = stack.pop()
            if node[0].left is None and node[0].right is None and node[1] == 'l':
                result += node[0].val
            else:
                if node[0].left is not None:
                    stack.append((node[0].left, 'l'))
                if node[0].right is not None:
                    stack.append((node[0].right, 'r'))
        return result