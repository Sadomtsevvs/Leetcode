import heapq

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        heap = []
        heapq.heapify(heap)

        stack = [(0, 0, root)]
        while stack:
            col, row, node = stack.pop()
            heapq.heappush(heap, (col, row, node.val))
            if node.left:
                stack.append((col - 1, row + 1, node.left))
            if node.right:
                stack.append((col + 1, row + 1, node.right))

        result = []
        prev_col = heap[0][0]
        level = []

        while heap:
            col, row, val = heapq.heappop(heap)
            if col == prev_col:
                level.append(val)
            else:
                result.append(level)
                prev_col = col
                level = [val]
        result.append(level)

        return result
