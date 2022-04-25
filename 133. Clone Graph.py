# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        if not node:
            return node

        visited = dict()

        def deepcopy(n):
            if n.val not in visited:
                visited[n.val] = Node(n.val)
                visited[n.val].neighbors = [deepcopy(neighbor) for neighbor in n.neighbors]
            return visited[n.val]
            # if n.val in visited:
            #     new_node = visited[n.val]
            # else:
            #     new_node = Node(n.val)
            #     visited[n.val] = new_node
            #     new_node.neighbors = [deepcopy(neighbor) for neighbor in n.neighbors]
            # return new_node

        return deepcopy(node)


adjList = [[2,4],[1,3],[2,4],[1,3]]
# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
# Explanation: There are 4 nodes in the graph.
# 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

new = Solution().cloneGraph(adjList)
pass