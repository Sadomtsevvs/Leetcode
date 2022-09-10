# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root, val: int):
        if not root:
            return TreeNode(val)
        stack = [root]
        while stack:
            node = stack.pop()
            if val < node.val:
                if not node.left:
                    node.left = TreeNode(val)
                    return root
                stack.append(node.left)
            else:
                if not node.right:
                    node.right = TreeNode(val)
                    return root
                stack.append(node.right)

        # recursive solution from LC comments
        #
        # if root == None:
        #     return TreeNode(val=val)
        # if root.val <= val:
        #     root.right = self.insertIntoBST(root.right, val)
        # else:
        #     root.left = self.insertIntoBST(root.left, val)
        # return root


# Input: root = [4,2,7,1,3], val = 5
# Output: [4,2,7,1,3,5]

# Input
# [40,20,60,10,30,50,70]
# 25
# Output
# [40,25,60,20,null,50,70,10,30]
# Expected
# [40,20,60,10,30,50,70,null,null,25]

# _root = TreeNode(4, TreeNode(2, TreeNode(1),  TreeNode(3)), TreeNode(7))
# _val = 5



print(Solution().insertIntoBST(_root, _val))
pass
