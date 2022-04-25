import random


class Solution:

    def __init__(self, nums: list[int]):
        self.origin = nums[:]
        self.cur = nums

    def reset(self) -> list[int]:
        return self.origin

    def shuffle(self) -> list[int]:
        random.shuffle(self.cur)
        return self.cur


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

# Input
# ["Solution", "shuffle", "reset", "shuffle"]
# [[[1, 2, 3]], [], [], []]
# Output
# [null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]
#
# Explanation
# Solution
# solution = new
# Solution([1, 2, 3]);
# solution.shuffle(); // Shuffle
# the
# array[1, 2, 3] and
# return its
# result.
# // Any
# permutation
# of[1, 2, 3]
# must
# be
# equally
# likely
# to
# be
# returned.
# // Example:
# return [3, 1, 2]
# solution.reset(); // Resets
# the
# array
# back
# to
# its
# original
# configuration[1, 2, 3].Return[1, 2, 3]
# solution.shuffle(); // Returns
# the
# random
# shuffling
# of
# array[1, 2, 3].Example:
# return [1, 3, 2]