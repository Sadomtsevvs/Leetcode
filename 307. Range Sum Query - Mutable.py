from typing import List


class Node:

    def __init__(self, beg, end, val=0):
        self.beg = beg
        self.end = end
        self.val = val
        self.left = None
        self.right = None


class NumArray:

    def __init__(self, nums: List[int]):

        def create_tree(beg, end):

            if beg == end:
                return Node(beg, beg, nums[beg])

            node = Node(beg, end)

            mid = (end + beg) // 2

            node.left = create_tree(beg, mid)
            node.right = create_tree(mid+1, end)
            node.val = node.left.val + node.right.val

            return node

        self.root = create_tree(0, len(nums) - 1)

    def update(self, index: int, val: int) -> None:

        def update_node(node, i, value):

            if node.beg == i and node.end == i:
                node.val = value
                return

            mid = (node.beg + node.end) // 2

            if i <= mid:
                update_node(node.left, i, val)
            else:
                update_node(node.right, i, val)

            node.val = node.left.val + node.right.val

        update_node(self.root, index, val)

    def sumRange(self, left: int, right: int) -> int:

        def sum_node(node, beg, end):

            if node.beg == beg and node.end == end:
                return node.val

            mid = (node.beg + node.end) // 2

            if end <= mid:
                return sum_node(node.left, beg, end)
            elif beg > mid:
                return sum_node(node.right, beg, end)
            else:
                return sum_node(node.left, beg, mid) + sum_node(node.right, mid+1, end)

        return sum_node(self.root, left, right)


# class NumArray:
#     first solution, TLE because of update function, O(n)
#
#     def __init__(self, nums: List[int]):
#         self.nums = nums
#         self.trail = []
#         s = 0
#         for num in nums:
#             s += num
#             self.trail.append(s)
#
#     def update(self, index: int, val: int) -> None:
#         diff = val - self.nums[index]
#         self.nums[index] = val
#         for i in range(index, len(self.nums)):
#             self.trail[i] += diff
#
#     def sumRange(self, left: int, right: int) -> int:
#         if left == 0:
#             return self.trail[right]
#         else:
#             return self.trail[right] - self.trail[left - 1]

# segment tree from LC comments, great solution, O(logn) update and O(logn) sum
#
# """
#     The idea here is to build a segment tree. Each node stores the left and right
#     endpoint of an interval and the sum of that interval. All of the leaves will store
#     elements of the array and each internal node will store sum of leaves under it.
#     Creating the tree takes O(n) time. Query and updates are both O(log n).
# """
#
#
# # Segment tree node
# class Node(object):
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#         self.total = 0
#         self.left = None
#         self.right = None
#
#
# class NumArray(object):
#     def __init__(self, nums):
#         """
#         initialize your data structure here.
#         :type nums: List[int]
#         """
#
#         # helper function to create the tree from input array
#         def createTree(nums, l, r):
#
#             # base case
#             if l > r:
#                 return None
#
#             # leaf node
#             if l == r:
#                 n = Node(l, r)
#                 n.total = nums[l]
#                 return n
#
#             mid = (l + r) // 2
#
#             root = Node(l, r)
#
#             # recursively build the Segment tree
#             root.left = createTree(nums, l, mid)
#             root.right = createTree(nums, mid + 1, r)
#
#             # Total stores the sum of all leaves under root
#             # i.e. those elements lying between (start, end)
#             root.total = root.left.total + root.right.total
#
#             return root
#
#         self.root = createTree(nums, 0, len(nums) - 1)
#
#     def update(self, i, val):
#         """
#         :type i: int
#         :type val: int
#         :rtype: int
#         """
#
#         # Helper function to update a value
#         def updateVal(root, i, val):
#
#             # Base case. The actual value will be updated in a leaf.
#             # The total is then propogated upwards
#             if root.start == root.end:
#                 root.total = val
#                 return val
#
#             mid = (root.start + root.end) // 2
#
#             # If the index is less than the mid, that leaf must be in the left subtree
#             if i <= mid:
#                 updateVal(root.left, i, val)
#
#             # Otherwise, the right subtree
#             else:
#                 updateVal(root.right, i, val)
#
#             # Propogate the changes after recursive call returns
#             root.total = root.left.total + root.right.total
#
#             return root.total
#
#         return updateVal(self.root, i, val)
#
#     def sumRange(self, i, j):
#         """
#         sum of elements nums[i..j], inclusive.
#         :type i: int
#         :type j: int
#         :rtype: int
#         """
#
#         # Helper function to calculate range sum
#         def rangeSum(root, i, j):
#
#             # If the range exactly matches the root, we already have the sum
#             if root.start == i and root.end == j:
#                 return root.total
#
#             mid = (root.start + root.end) // 2
#
#             # If end of the range is less than the mid, the entire interval lies
#             # in the left subtree
#             if j <= mid:
#                 return rangeSum(root.left, i, j)
#
#             # If start of the interval is greater than mid, the entire inteval lies
#             # in the right subtree
#             elif i >= mid + 1:
#                 return rangeSum(root.right, i, j)
#
#             # Otherwise, the interval is split. So we calculate the sum recursively,
#             # by splitting the interval
#             else:
#                 return rangeSum(root.left, i, mid) + rangeSum(root.right, mid + 1, j)
#
#         return rangeSum(self.root, i, j)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

# numArray = NumArray([1, 3, 5])
# print(numArray.sumRange(0, 2))  # return 1 + 3 + 5 = 9
# numArray.update(1, 2)   # nums = [1, 2, 5]
# print(numArray.sumRange(0, 2))  # return 1 + 2 + 5 = 8

# numArray = NumArray([9, -8])
# numArray.update(0, 3)
# print(numArray.sumRange(1, 1))
# print(numArray.sumRange(0, 1))
# numArray.update(1, -3)
# print(numArray.sumRange(0, 1))

# ["NumArray","sumRange","sumRange","sumRange","update","update","update","sumRange","update","sumRange","update"]
# [[[0,9,5,7,3]],[4,4],[2,4],[3,3],[4,5],[1,7],[0,8],[1,2],[1,9],[4,4],[3,4]]
numArray = NumArray([0,9,5,7,3])
print(numArray.sumRange(4, 4))
