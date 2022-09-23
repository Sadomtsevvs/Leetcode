# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        # my first solution, TLE, MLE
        #
        # def lca(node, one, two):
        #     if not node:
        #         return None
        #     if node.val == one or node.val == two:
        #         return node
        #     left = lca(node.left, one, two)
        #     right = lca(node.right, one, two)
        #     if left and right:
        #         return node
        #     return left or right
        #
        # lca_node = lca(root, startValue, destValue)
        #
        # def find_path(node, goal, path):
        #     if not node:
        #         return None
        #     if node.val == goal:
        #         return path
        #     left_path = find_path(node.left, goal, path + 'L')
        #     if left_path:
        #         return left_path
        #     return find_path(node.right, goal, path + 'R')
        #
        # path_to_start = find_path(lca_node, startValue, '')
        # path_to_dest = find_path(lca_node, destValue, '')
        #
        # return "U" * len(path_to_start) + path_to_dest

        def find_path(node, goal):
            if node.val == goal:
                return ""
            if node.left:
                left_path = find_path(node.left, goal)
                if isinstance(left_path, str):
                    return 'L' + left_path
            if node.right:
                right_path = find_path(node.right, goal)
                if isinstance(right_path, str):
                    return 'R' + right_path
            return None

        path_to_start = find_path(root, startValue)
        path_to_dest = find_path(root, destValue)

        i, j = 0, 0
        while i < len(path_to_start) and j < len(path_to_dest) and path_to_start[i] == path_to_dest[j]:
            i += 1
            j += 1

        return "U" * len(path_to_start[i:]) + path_to_dest[j:]

        # votrubac solution
        #
        # def find(n: TreeNode, val: int, path: List[str]) -> bool:
        #     if n.val == val:
        #         return True
        #     if n.left and find(n.left, val, path):
        #         path += "L"
        #     elif n.right and find(n.right, val, path):
        #         path += "R"
        #     return path
        # s, d = [], []
        # find(root, startValue, s)
        # find(root, destValue, d)
        # while len(s) and len(d) and s[-1] == d[-1]:
        #     s.pop()
        #     d.pop()
        # return "".join("U" * len(s)) + "".join(reversed(d))

        # LCA solution from comments, the second part is iterative, not recursive as mine
        #
        # def lca(node):
        #     """Return lowest common ancestor of start and dest nodes."""
        #     if not node or node.val in (startValue, destValue): return node
        #     left, right = lca(node.left), lca(node.right)
        #     return node if left and right else left or right
        # 
        # root = lca(root)  # only this sub-tree matters
        #
        # ps = pd = ""
        # stack = [(root, "")]
        # while stack:
        #     node, path = stack.pop()
        #     if node.val == startValue: ps = path
        #     if node.val == destValue: pd = path
        #     if node.left: stack.append((node.left, path + "L"))
        #     if node.right: stack.append((node.right, path + "R"))
        # return "U" * len(ps) + pd