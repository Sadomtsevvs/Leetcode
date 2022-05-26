# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:

        # my solution, recursive
        #
        # def change_node(node):
        #
        #     if not node:
        #         return
        #
        #     right = node.right
        #
        #     node.right = change_node(node.left)
        #     node.left = None
        #
        #     tail = node
        #     while tail.right is not None:
        #         tail = tail.right
        #
        #     tail.right = change_node(right)
        #
        #     return node
        #
        # change_node(root)

        # from LC
        cur = root
        while cur:
            if cur.left:
                last = cur.left
                while last.right is not None:
                    last = last.right
                last.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right

        # from LC
        #
        if not root:
            return
        right = root.right
        if root.left:
            self.flatten(root.left)
            tail = root.left
            while tail.right:
                tail = tail.right
            root.left, root.right, tail.right = None, root.left, right
        self.flatten(right)