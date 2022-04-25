# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root, k: int) -> int:

        # my solution, too complex, I think

        kk = k

        def dfs(node):
            nonlocal kk
            if node is None:
                return
            res = dfs(node.left)
            if res is not None:
                return res
            kk -= 1
            if kk == 0:
                return node.val
            res = dfs(node.right)
            if res is not None:
                return res

        return dfs(root)

        # 1 official solution
        #
        # def inorder(r):
        #     return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        #
        # return inorder(root)[k - 1]

        # 2 official solution
        #
        # stack = []
        #
        # while True:
        #     while root:
        #         stack.append(root)
        #         root = root.left
        #     root = stack.pop()
        #     k -= 1
        #     if not k:
        #         return root.val
        #     root = root.right


tree = TreeNode(5, TreeNode(2, None, TreeNode(4, TreeNode(3), None)), TreeNode(7))
print(Solution().kthSmallest(tree, 5))