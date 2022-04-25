from itertools import accumulate


class NumArray:

    def __init__(self, nums: list[int]):
        self.pref = list(accumulate([0] + nums))
        # self.pref = list(accumulate(nums, initial=0))

    def sumRange(self, left: int, right: int) -> int:
        return self.pref[right+1] - self.pref[left]


# Your NumArray object will be instantiated and called as such:
# nums = [-2, 0, 3, -5, 2, -1]
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
