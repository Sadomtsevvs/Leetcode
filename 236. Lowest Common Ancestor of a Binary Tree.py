# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

""" 1. not efficient solution

def val_in_tree(val, tree):
    if not tree:
        return False
    if val == tree.val:
        return True
    return val_in_tree(val, tree.left) or val_in_tree(val, tree.right)


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val == p.val or root.val == q.val:
            return root
        p_in_left = True if val_in_tree(p.val, root.left) else False
        q_in_left = True if val_in_tree(q.val, root.left) else False
        if p_in_left and q_in_left:
            return self.lowestCommonAncestor(root.left, p, q)
        if not p_in_left and not q_in_left:
            return self.lowestCommonAncestor(root.right, p, q)
        return root

"""

# 2. more efficient solution, but still ugly

def path_to_val(val, tree, path=''):
    if not tree:
        return None
    if val == tree.val:
        return path
    left_path = path_to_val(val, tree.left, path + 'l')
    if left_path is None:
        return path_to_val(val, tree.right, path + 'r')
    else:
        return left_path


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val == p.val or root.val == q.val:
            return root
        path_to_p = path_to_val(p.val, root)
        path_to_q = path_to_val(q.val, root)
        cur_ancestor = root
        for i in range(min(len(path_to_p), len(path_to_q))):
            if path_to_p[i] != path_to_q[i]:
                return cur_ancestor
            elif path_to_p[i] == 'l':
                cur_ancestor = cur_ancestor.left
            else:
                cur_ancestor = cur_ancestor.right
        return cur_ancestor

        # from LC comments
        #
        # If looking for me, return myself
        # if root == p or root == q:
        #     return root
        #
        # left = right = None
        # # else look in left and right child
        # if root.left:
        #     left = self.lowestCommonAncestor(root.left, p, q)
        # if root.right:
        #     right = self.lowestCommonAncestor(root.right, p, q)
        #
        # # if both children returned a node, means
        # # both p and q found so parent is LCA
        # if left and right:
        #     return root
        # else:
        #     # either one of the chidren returned a node, meaning either p or q found on left or right branch.
        #     # Example: assuming 'p' found in left child, right child returned 'None'. This means 'q' is
        #     # somewhere below node where 'p' was found we dont need to search all the way,
        #     # because in such scenarios, node where 'p' found is LCA
        #     return left or right