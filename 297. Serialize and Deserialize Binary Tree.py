# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return ''
        result = []
        stack = [root]
        while stack:
            this_level = []
            next_stack = []
            for node in stack:
                if node:
                    this_level.append(str(node.val))
                    next_stack.append(node.left)
                    next_stack.append(node.right)
                else:
                    this_level.append('')
            result.append(','.join(this_level))
            stack = next_stack
        return '|'.join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        root = None
        parents = []
        for level in data.split('|'):
            i = -1
            new_parents = []
            for val in level.split(','):
                i += 1
                if val == '':
                    continue
                node = TreeNode(int(val))
                if parents:
                    if i % 2 == 0:
                        parents[i//2].left = node
                    else:
                        parents[i//2].right = node
                else:
                    root = node
                new_parents.append(node)
            parents = new_parents
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
