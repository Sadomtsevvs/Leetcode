# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # bfs
        stack = [root]
        while stack:
            ans = 0
            next_stack = []
            for node in stack:
                ans += node.val
                if node.left:
                    next_stack.append(node.left)
                if node.right:
                    next_stack.append(node.right)
            stack = next_stack
        return ans

        # dfs
        # ans = 0
        # max_depth = -1
        #
        # def dfs(node, depth):
        #     nonlocal ans, max_depth
        #     if not node:
        #         return
        #     if depth > max_depth:
        #         max_depth = depth
        #         ans = node.val
        #     elif depth == max_depth:
        #         ans += node.val
        #     dfs(node.left, depth + 1)
        #     dfs(node.right, depth + 1)
        #
        # dfs(root, 0)
        # return ans


        # solution from Lee
        #
        # q = [root]
        # while q:
        #     pre, q = q, [child for p in q for child in [p.left, p.right] if child]
        # return sum(node.val for node in pre)
