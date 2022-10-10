# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        nodes =[root]
        for node in nodes:
            if (k - node.val) in seen:
                return True
            seen.add(node.val)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        return False

        # my first solution
        #
        # seen = set()
        #
        # def dfs(node):
        #
        #     if not node:
        #         return False
        #
        #     if (k - node.val) in seen:
        #         return True
        #     else:
        #         seen.add(node.val)
        #
        #     if dfs(node.right):
        #         return True
        #     if dfs(node.left):
        #         return True
        #
        #     return False
        #
        # return dfs(root)