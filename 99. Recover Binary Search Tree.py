class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:

        # minus_inf_node = TreeNode(-float("inf"))
        # plus_inf_node = TreeNode(float("inf"))
        #
        # def dfs(node, min_node, max_node):
        #     if not node:
        #         return False
        #     if node.val < min_node.val:
        #         return (node, min_node)
        #     elif node.val > max_node.val:
        #         return (node, max_node)
        #     dfs_left = dfs(node.left, min_node, node)
        #     dfs_right = dfs(node.right, node, max_node)
        #     if dfs_left and dfs_right:
        #         return (dfs_left[0], dfs_right[0])
        #     return dfs_left or dfs_right
        #
        # node1, node2 = dfs(root, minus_inf_node, plus_inf_node)
        #
        # node1.val, node2.val = node2.val, node1.val

        # from LC comments
        #

        self.first = self.second = self.prev = None

        # the idea is the in order BST is always increasing, if not, then there is something wrong
        def inorderBST(node):

            if not node:
                return

            # track left side to start with min
            inorderBST(node.left)

            # so that the first prev is the smallest node
            # and update each time
            if self.prev:

                # when order is wrong
                # check the examples in the illustration
                if self.prev.val > node.val:
                    if not self.first:
                        self.first = self.prev
                    self.second = node

            # update the prev node
            self.prev = node

            # check right side
            inorderBST(node.right)

        # self.first = self.second = self.prev = None
        inorderBST(root)

        # swap the two wrong ones
        self.first.val, self.second.val = self.second.val, self.first.val


_root = TreeNode(3, TreeNode(1), TreeNode(4, TreeNode(2)))
_root = TreeNode(2, TreeNode(3), TreeNode(1))
_root = TreeNode(3, None, TreeNode(2, None, TreeNode(1)))
# Input: root = [3,1,4,null,null,2]
# Output: [2,1,4,null,null,3]
# Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.

print(Solution().recoverTree(_root))
pass