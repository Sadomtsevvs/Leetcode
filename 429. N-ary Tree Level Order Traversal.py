"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> list[list[int]]:
        result = []
        if root is None:
            return result
        parents = [root]
        while parents:
            result.append([p.val for p in parents])
            parents = [child for parent in parents for child in parent.children]
        return result