# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        if not root:
            return []

        result = []

        def dfs(node, cur_path, sum_to_reach):
            if not node.left and not node.right and sum_to_reach == 0:
                result.append(cur_path)
            if node.left:
                dfs(node.left, cur_path + [node.left.val], sum_to_reach - node.left.val)
            if node.right:
                dfs(node.right, cur_path + [node.right.val], sum_to_reach - node.right.val)

        dfs(root, [root.val], targetSum - root.val)

        return result
