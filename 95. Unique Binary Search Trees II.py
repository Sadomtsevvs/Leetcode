# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int):

        # I can't solve this
        #
        # nums = set(range(1, n + 1))
        #
        # result = []
        #
        # def backtrack(cur_head, cur_tree, remain_nums, restrict_nums):
        #     if len(remain_nums) == 0:
        #         result.append(TreeNode(cur_head.val, cur_head.left, cur_head.right))
        #         return
        #     for remain_num in remain_nums:
        #         if remain_num in restrict_nums:
        #             continue
        #         cur_restrict_nums = set()
        #         if remain_num < cur_tree.val:
        #             for rr in remain_nums - {remain_num}:
        #                 if rr > cur_tree.val:
        #                     cur_restrict_nums.add(rr)
        #             cur_tree.left = TreeNode(remain_num)
        #             backtrack(cur_head, cur_tree.left, remain_nums - {remain_num}, restrict_nums | cur_restrict_nums)
        #         else:
        #             for rr in remain_nums - {remain_num}:
        #                 if rr < cur_tree.val:
        #                     cur_restrict_nums.add(rr)
        #             cur_tree.right = TreeNode(remain_num)
        #             backtrack(cur_head, cur_tree.right, remain_nums - {remain_num}, restrict_nums | cur_restrict_nums)
        #
        # for num in nums:
        #     head = TreeNode(num)
        #     backtrack(head, head, nums - {num}, set())
        #
        # return result

        # solution from LC comments
        #
        def f(n, labels):
            if n == 0:
                return [None]

            return [
                TreeNode(labels[i], l, r)  # take the ith element to make it inorder traversal
                for i in range(n)  # try children of all sizes
                for l in f(i, labels[:i])  # put left children of size i
                for r in f(n - 1 - i, labels[i + 1:])  # put right the rest of the children up to n-1
            ]

        return f(n, list(range(1, n + 1)))

        # my solution after reading official
        #
        # def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        #
        #     def trees(start, end, memo):
        #
        #         res = []
        #
        #         if start > end:
        #             return [None]
        #         if (start, end) in memo:
        #             return memo[(start, end)]
        #
        #         for i in range(start, end + 1):
        #             lefts = trees(start, i - 1, memo)
        #             rights = trees(i + 1, end, memo)
        #
        #             for left in lefts:
        #                 for right in rights:
        #                     res.append(TreeNode(i, left, right))
        #
        #         memo[(start, end)] = res
        #
        #         return res
        #
        #     return trees(1, n, {})


#
# Input: n = 3
# Output: [[1, null, 2, null, 3], [1, null, 3, 2], [2, 1, 3], [3, 1, null, null, 2], [3, 2, null, 1]]
_n = 3

res = Solution().generateTrees(_n)
print(res)