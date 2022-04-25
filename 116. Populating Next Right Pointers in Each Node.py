# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        parents = [root]
        while parents:
            for i in range(len(parents) - 1):
                parents[i].next = parents[i+1]
            next_nodes = []
            for parent in parents:
                if parent.left is not None:
                    next_nodes.append(parent.left)
                    next_nodes.append(parent.right)
            parents = next_nodes
        return root


_root = Node(0, Node(1), Node(2))
_new_root = Solution().connect(_root)
pass