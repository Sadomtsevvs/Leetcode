"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> list[int]:

        # recursive solution is trivial as mentioned in description
        #
        # if not root:
        #     return []
        # ans = [root.val]
        # for child in root.children:
        #     ans += self.preorder(child)
        # return ans

        if not root:
            return []

        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            ans.append(node.val)
            for child in reversed(node.children):
                stack.append(child)
        return ans