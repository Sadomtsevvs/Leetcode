from  collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> list[Optional[TreeNode]]:

        result = []
        paths = defaultdict(int)

        def get_path(node):
            if not node:
                return "None"
            else:
                path = str(node.val)
            path += '.' + get_path(node.left)
            path += '.' + get_path(node.right)
            paths[path] += 1
            if paths[path] == 2:
                result.append(node)
            return path

        get_path(root)

        return result

        # bfs('', root)

        # stack = [root]
        # while stack:
        #     node = stack.pop()