# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # find parents of the target with dfs
        parents = []
        stack = [(root, parents)]
        while stack:
            node, parents = stack.pop()
            if not node:
                continue
            if node == target:
                target_node = node
                break
            stack.append((node.left, parents + [node]))
            stack.append((node.right, parents + [node]))
        result = []
        # lets' check all children of target with bfs
        stack = [(target_node, 0)]
        while stack:
            next_stack = []
            while stack:
                node, level = stack.pop()
                if not node:
                    continue
                if level == k:
                    result.append(node.val)
                else:
                    next_stack.append((node.left, level + 1))
                    next_stack.append((node.right, level + 1))
            stack = next_stack
        # let's check all target's parents children with bfs
        seen = {target_node}
        for i in range(len(parents) - 1, max(len(parents) - k - 1, -1), -1):
            i_k = k - len(parents) + i
            stack = [(parents[i], 0)]
            while stack:
                next_stack = []
                while stack:
                    node, level = stack.pop()
                    if not node:
                        continue
                    if node in seen:
                        continue
                    if level == i_k:
                        result.append(node.val)
                    else:
                        seen.add(node)
                        next_stack.append((node.left, level + 1))
                        next_stack.append((node.right, level + 1))
                stack = next_stack
        return result


_target = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4)))
_root = TreeNode(3, _target, TreeNode(1, TreeNode(0), TreeNode(8)))
_k = 2
_target = TreeNode(1)
_root = _target
_k = 3
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
# Output: [7,4,1]
# Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
print(Solution().distanceK(_root, _target, _k))
