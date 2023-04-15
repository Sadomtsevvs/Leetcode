from time import time
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        next_nodes = {None: [root, root.val]}
        sum_level = root.val
        while next_nodes:
            next_next_nodes = dict()
            next_sum_level = 0
            for next_node in next_nodes.items():
                sum_parent = next_node[1][-1]
                for i in range(len(next_node[1]) - 1):
                    node = next_node[1][i]
                    if not node:
                        continue
                    node.val = sum_level - sum_parent
                    children = []
                    sum_brothers = 0
                    children.append(node.left)
                    children.append(node.right)
                    if node.left:
                        sum_brothers += node.left.val
                    if node.right:
                        sum_brothers += node.right.val
                    children.append(sum_brothers)
                    next_next_nodes[node] = children
                    next_sum_level += sum_brothers
            next_nodes = next_next_nodes
            sum_level = next_sum_level
        return root


start_time = time()

# Input: root = [5,4,9,1,10,null,7]
# Output: [0,0,0,7,7,null,11]
# Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
# - Node with value 5 does not have any cousins so its sum is 0.
# - Node with value 4 does not have any cousins so its sum is 0.
# - Node with value 9 does not have any cousins so its sum is 0.
# - Node with value 1 has a cousin with value 7 so its sum is 7.
# - Node with value 10 has a cousin with value 7 so its sum is 7.
# - Node with value 7 has cousins with values 1 and 10 so its sum is 11.

_root = TreeNode(5, TreeNode(4, TreeNode(1), TreeNode(10)), TreeNode(9, None, TreeNode(7)))

Solution().replaceValueInTree(_root)

print("--- %s seconds ---" % (time() - start_time))
