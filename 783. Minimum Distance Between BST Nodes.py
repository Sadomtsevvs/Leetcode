import heapq
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        heap = []
        heapq.heapify(heap)
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            heapq.heappush(heap, node.val)
            stack.append(node.left)
            stack.append(node.right)
        min_diff = float('inf')
        first = heapq.heappop(heap)
        while heap:
            second = heapq.heappop(heap)
            min_diff = min(min_diff, second - first)
            first = second
        return min_diff
