from time import time


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:

        def min_tail_sum(mx, count):
            if count == 0:
                return 0
            result = 0
            if count >= mx:
                result += count - mx + 1
            elif count + 1 < mx:
                diff = mx - count - 1
                result -= diff * (diff + 1) // 2
            return result + mx * (mx - 1) // 2

        beg, end = 1, maxSum - (n - 1)
        while beg <= end:
            mid = (beg + end) // 2
            if mid + min_tail_sum(mid, index) + min_tail_sum(mid, n - index - 1) <= maxSum:
                beg = mid + 1
            else:
                end = mid - 1

        return beg - 1


start_time = time()

# Example 1:
# Input: n = 4, index = 2,  maxSum = 6
_n = 4
_index = 2
_maxSum = 6
# Output: 2
# Explanation: nums = [1,2,2,1] is one array that satisfies all the conditions.
# There are no arrays that satisfy all the conditions and have nums[2] == 3, so 2 is the maximum nums[2].
#
# Example 2:
# Input: n = 6, index = 1,  maxSum = 10
# _n = 6
# _index = 1
# _maxSum = 10
# Output: 3

# _n = 9
# _index = 0
# _maxSum = 90924720

# _n = 9790
# _index = 381
# _maxSum = 755841990

print(Solution().maxValue(_n, _index, _maxSum))

print("--- %s seconds ---" % (time() - start_time))
