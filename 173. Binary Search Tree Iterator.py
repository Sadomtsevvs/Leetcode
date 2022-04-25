# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):

        def inorder(node):
            if node is None:
                return
            result = []
            left = inorder(node.left)
            if left:
                result += left
            result += [node.val]
            right = inorder(node.right)
            if right:
                result += right
            return result

        self.inorder = inorder(root)
        self.point = -1

    def next(self) -> int:
        self.point += 1
        return self.inorder[self.point]

    def hasNext(self) -> bool:
        return self.point + 1 < len(self.inorder)

# solution from LC comments
#
# class BSTIterator(object):
#     def __init__(self, root):
#         self.st = []
#         self.pushLeft(root)
#
#     def pushLeft(self, root):
#         while root != None:
#             self.st.append(root)
#             root = root.left
#
#     def next(self):
#         node = self.st.pop()
#         self.pushLeft(node.right)
#         return node.val
#
#     def hasNext(self):
#         return len(self.st) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()