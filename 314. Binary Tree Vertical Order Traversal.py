# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return root

        res = [[] for _ in range(201)]

        bfs = [(root, 100)]

        while bfs:
            next_bfs = []
            for node, idx in bfs:
                res[idx].append(node.val)
                if node.left:
                    next_bfs.append((node.left, idx - 1))
                if node.right:
                    next_bfs.append((node.right, idx + 1))
            bfs = next_bfs

        return [nodes for nodes in res if nodes]

        # dfs is not working because we have to make VERTICAL traverse
        #
        # if not root:
        #     return root
        # res = [[] for _ in range(201)]
        #
        # def dfs(node, idx):
        #     if not node:
        #         return
        #     res[idx].append(node.val)
        #     dfs(node.left, idx - 1)
        #     dfs(node.right, idx + 1)
        #
        # dfs(root, 100)
        #
        # return [nodes for nodes in res if nodes]

        # official solution
        #
        # if root is None:
        #     return []
        #
        # columnTable = defaultdict(list)
        # min_column = max_column = 0
        # queue = deque([(root, 0)])
        #
        # while queue:
        #     node, column = queue.popleft()
        #
        #     if node is not None:
        #         columnTable[column].append(node.val)
        #         min_column = min(min_column, column)
        #         max_column = max(max_column, column)
        #
        #         queue.append((node.left, column - 1))
        #         queue.append((node.right, column + 1))
        #
        # return [columnTable[x] for x in range(min_column, max_column + 1)]