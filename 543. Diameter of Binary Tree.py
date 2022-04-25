class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root) -> int:

        ans = [0]

        def dfs(node):

            if not node:
                return -1

            left = dfs(node.left) + 1
            right = dfs(node.right) + 1

            ans[0] = max(ans[0], left + right)

            return max(left, right)

        dfs(root)

        return ans[0]

        # from LC comments
        #
        # self.ans = 0
        #
        # def depth(p):
        #     if not p: return 0
        #     left, right = depth(p.left), depth(p.right)
        #     self.ans = max(self.ans, left + right)
        #     return 1 + max(left, right)
        #
        # depth(root)
        # return self.ans


_root = TreeNode(1, TreeNode(2,TreeNode(4),TreeNode(5)), TreeNode(3))
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

print(Solution().diameterOfBinaryTree(_root))