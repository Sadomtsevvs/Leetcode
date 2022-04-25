# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def the_leftest_node(node):
            cur = node
            while cur.left:
                cur = cur.left
            return cur

        parent = None
        left_branch = None
        node_to_del = root
        while node_to_del and node_to_del.val != key:
            parent = node_to_del
            if node_to_del.val > key:
                left_branch = True
                node_to_del = node_to_del.left
            else:
                left_branch = False
                node_to_del = node_to_del.right

        if not node_to_del:
            return root

        if node_to_del.left is None:
            if parent:
                if left_branch:
                    parent.left = node_to_del.right
                else:
                    parent.right = node_to_del.right
            else:
                root = node_to_del.right
        elif node_to_del.right is None:
            if parent:
                if left_branch:
                    parent.left = node_to_del.left
                else:
                    parent.right = node_to_del.left
            else:
                root = node_to_del.left
        else:
            leftest = the_leftest_node(node_to_del.right)
            leftest.left = node_to_del.left
            if parent:
                if left_branch:
                    parent.left = node_to_del.right
                else:
                    parent.right = node_to_del.right
            else:
                root = node_to_del.right
        return root


#       LC comment solution
#
#         if(root == null) return null;
#         if(root.val == key) {
#             return mergeTwoTrees(root.left, root.right);
#         }
#         if(key< root.val){
#             root.left = deleteNode(root.left, key);
#         } else {
#             root.right = deleteNode(root.right, key);
#         }
#         return root;
#     }
#     private TreeNode mergeTwoTrees(TreeNode left, TreeNode right) {
#         if(left == null && right == null){ return null;}
#         if(right == null) { return left;}
#         if(left == null) {return right;}
#         TreeNode traverse = right;
#         while(traverse.left != null) {
#             traverse = traverse.left;
#         }
#         traverse.left = left;
#         return right;
#     }
# }