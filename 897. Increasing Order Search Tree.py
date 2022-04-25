# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:

        stack = []

        def traverse(node):
            if not node:
                return
            traverse(node.right)
            stack.append(node.val)
            traverse(node.left)

        traverse(root)

        dummy = node = TreeNode()

        while stack:
            node.right = TreeNode(stack.pop())
            node = node.right

        return dummy.right

        # official solution 1
        #
        # def inorder(node):
        #     if node:
        #         yield from inorder(node.left)
        #         yield node.val
        #         yield from inorder(node.right)
        #
        # ans = cur = TreeNode(None)
        # for v in inorder(root):
        #     cur.right = TreeNode(v)
        #     cur = cur.right
        # return ans.right

        # official solution 2
        #
        # def inorder(node):
        #     if node:
        #         inorder(node.left)
        #         node.left = None
        #         self.cur.right = node
        #         self.cur = node
        #         inorder(node.right)
        #
        # ans = self.cur = TreeNode(None)
        # inorder(root)
        # return ans.right
