from time import time


class Solution:
    def minimumAverageDifference(self, nums: list[int]) -> int:
        n = len(nums)
        left, right = [0]*n, [0]*n
        left_sum = 0
        right_sum = 0
        for i in range(n):
            left_sum = nums[i] + left_sum
            left[i] = left_sum //(i+1)
            right_sum = nums[n-i-1] + right_sum
            right[i] = right_sum //(i+1)
        right[-1] = 0
        avrg = float('inf')
        ans = -1
        for i in range(n):
            res = abs(left[i] - right[n-2-i])
            if res < avrg:
                avrg = res
                ans = i
        return ans


start_time = time()

_nums = [2,5,3,9,5,3]
_nums = [0]
# Input: nums = [2,5,3,9,5,3]
# Output: 3
# Explanation:
# - The average difference of index 0 is: |2 / 1 - (5 + 3 + 9 + 5 + 3) / 5| = |2 / 1 - 25 / 5| = |2 - 5| = 3.
# - The average difference of index 1 is: |(2 + 5) / 2 - (3 + 9 + 5 + 3) / 4| = |7 / 2 - 20 / 4| = |3 - 5| = 2.
# - The average difference of index 2 is: |(2 + 5 + 3) / 3 - (9 + 5 + 3) / 3| = |10 / 3 - 17 / 3| = |3 - 5| = 2.
# - The average difference of index 3 is: |(2 + 5 + 3 + 9) / 4 - (5 + 3) / 2| = |19 / 4 - 8 / 2| = |4 - 4| = 0.
# - The average difference of index 4 is: |(2 + 5 + 3 + 9 + 5) / 5 - 3 / 1| = |24 / 5 - 3 / 1| = |4 - 3| = 1.
# - The average difference of index 5 is: |(2 + 5 + 3 + 9 + 5 + 3) / 6 - 0| = |27 / 6 - 0| = |4 - 0| = 4.
# The average difference of index 3 is the minimum average difference so return 3.

print(Solution().minimumAverageDifference(_nums))

print("--- %s seconds ---" % (time() - start_time))
