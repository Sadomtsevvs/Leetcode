from time import time
import heapq


class Solution:
    def halveArray(self, nums: list[int]) -> int:
        cur_sum = sum(nums)
        target = cur_sum / 2
        heap = []
        heapq.heapify(heap)
        for num in nums:
            heapq.heappush(heap, -num)
        result = 0
        while cur_sum > target:
            biggest = - heapq.heappop(heap)
            half_biggest = biggest / 2
            heapq.heappush(heap, -half_biggest)
            cur_sum -= half_biggest
            result += 1
        return result


start_time = time()

_nums = [5,19,8,1]
_nums = [3,8,20]
# Input: nums = [5,19,8,1]
# Output: 3
# Explanation: The initial sum of nums is equal to 5 + 19 + 8 + 1 = 33.
# The following is one of the ways to reduce the sum by at least half:
# Pick the number 19 and reduce it to 9.5.
# Pick the number 9.5 and reduce it to 4.75.
# Pick the number 8 and reduce it to 4.
# The final array is [5, 4.75, 4, 1] with a total sum of 5 + 4.75 + 4 + 1 = 14.75.
# The sum of nums has been reduced by 33 - 14.75 = 18.25, which is at least half of the initial sum, 18.25 >= 33/2 = 16.5.
# Overall, 3 operations were used so we return 3.
# It can be shown that we cannot reduce the sum by at least half in less than 3 operations.

print(Solution().halveArray(_nums))

print("--- %s seconds ---" % (time() - start_time))