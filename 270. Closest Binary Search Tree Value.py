# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        if not root:
            return root

        if root.val == target:
            return root.val

        if root.val > target:
            if not root.left:
                return root.val
            child = self.closestValue(root.left, target);
            if abs(target - root.val) < abs(target - child):
                return root.val
            else:
                return child
        else:
            if not root.right:
                return root.val
            child = self.closestValue(root.right, target);
            if abs(target - root.val) < abs(target - child):
                return root.val
            else:
                return child

            # official solution, great, without recursion
            #
            # closest = root.val
            # while root:
            #     closest = min(root.val, closest, key=lambda x: abs(target - x))
            #     root = root.left if target < root.val else root.right
            # return closest
