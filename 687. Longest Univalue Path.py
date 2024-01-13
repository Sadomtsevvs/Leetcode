from collections import Counter
from time import time


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        answer = 0

        def lup(node, prev):
            nonlocal answer
            if not node:
                return 0
            val = node.val
            left = lup(node.left, val)
            right = lup(node.right, val)
            answer = max(answer, left + right)
            if val != prev:
                return 0
            return 1 + max(left, right)

        lup(root, 1001)
        return answer


start_time = time()

# Example 1:
# Input: root = [5,4,5,1,1,null,5]
_root = [5,4,5,1,1,None,5]
# Output: 2
# Explanation: The shown image shows that the longest path of the same value (i.e. 5).
#
# Example 2:
# Input: root = [1,4,5,4,4,null,5]
# Output: 2
# Explanation: The shown image shows that the longest path of the same value (i.e. 4).

print(Solution().longestUnivaluePath(_root))

print("--- %s seconds ---" % (time() - start_time))
