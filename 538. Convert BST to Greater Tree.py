# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def change(node, cur):
            if not node:
                return cur
            node.val += change(node.right, cur)
            return change(node.left, node.val)

        change(root, 0)

        return root

    # official solution 1
    #
    # def __init__(self):
    #     self.total = 0
    #
    # def convertBST(self, root):
    #     if root is not None:
    #         self.convertBST(root.right)
    #         self.total += root.val
    #         root.val = self.total
    #         self.convertBST(root.left)
    #     return root

    # official solution 2
    #
    # def convertBST(self, root):
    #     total = 0
    #
    #     node = root
    #     stack = []
    #     while stack or node is not None:
    #         # push all nodes up to (and including) this subtree's maximum on
    #         # the stack.
    #         while node is not None:
    #             stack.append(node)
    #             node = node.right
    #
    #         node = stack.pop()
    #         total += node.val
    #         node.val = total
    #
    #         # all nodes with values between the current and its parent lie in
    #         # the left subtree.
    #         node = node.left
    #
    #     return root
