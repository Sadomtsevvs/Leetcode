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

    # from LC
    #
    # def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
    #     self.parent = {}
    #     self.getParents(root, None)
    #     return self.bfs(target, K)
    #
    # def getParents(self, node: TreeNode, parent: TreeNode) -> None:
    #     if node == None: return
    #
    #     self.parent[node.val] = parent
    #
    #     self.getParents(node.left, node)
    #     self.getParents(node.right, node)
    #
    # def bfs(self, start: TreeNode, K: int) -> List[int]:
    #     res, q, visited = [], [(start, 0)], set()
    #
    #     while q:
    #         n, d = q.pop(0)
    #
    #         if n not in visited:
    #             if d == K: res.append(n.val)
    #             visited.add(n)
    #
    #             if n.left: q.append((n.left, d + 1))
    #             if n.right: q.append((n.right, d + 1))
    #             if self.parent[n.val]: q.append((self.parent[n.val], d + 1))
    #
    #     return res

        # official solution
        #
        # def dfs(node, par = None):
        #     if node:
        #         node.par = par
        #         dfs(node.left, node)
        #         dfs(node.right, node)
        #
        # dfs(root)
        #
        # queue = collections.deque([(target, 0)])
        # seen = {target}
        # while queue:
        #     if queue[0][1] == K:
        #         return [node.val for node, d in queue]
        #     node, d = queue.popleft()
        #     for nei in (node.left, node.right, node.par):
        #         if nei and nei not in seen:
        #             seen.add(nei)
        #             queue.append((nei, d+1))
        #
        # return []


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
