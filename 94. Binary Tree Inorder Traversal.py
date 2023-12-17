# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:

        # iterative solution
        #
        if not root:
            return []
        result = []
        trav = []
        node = root
        while node:
            trav.append(node)
            node = node.left
        while trav:
            node = trav.pop()
            result.append(node.val)
            node = node.right
            while node:
                trav.append(node)
                node = node.left
        return result

        # iterative solution after reading official solution
        #
        # if not root:
        #     return []
        # result = []
        # trav = []
        # node = root
        # while node or trav:
        #     while node:
        #         trav.append(node)
        #         node = node.left
        #     node = trav.pop()
        #     result.append(node.val)
        #     node = node.right
        # return result

        # recursive solution
        #
        # if not root:
        #     return []
        # result = self.inorderTraversal(root.left)
        # result.append(root.val)
        # result += self.inorderTraversal(root.right)
        # return result
