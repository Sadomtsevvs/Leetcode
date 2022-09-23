from time import time
from typing import List


class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = 0
        for num in nums:
            if num % 2 == 0:
                even_sum += num

        result = []
        for val, ind in queries:
            cur_num = nums[ind]
            if cur_num % 2 == 0:
                even_sum -= cur_num
            cur_num += val
            nums[ind] = cur_num
            if cur_num % 2 == 0:
                even_sum += cur_num
            result.append(even_sum)

        return result


start_time = time()

_nums = [1,2,3,4]
_queries = [[1,0],[-3,1],[-4,0],[2,3]]
# Example 1:
# Input: nums = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
# Output: [8,6,2,4]
# Explanation: At the beginning, the array is [1,2,3,4].
# After adding 1 to nums[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
# After adding -3 to nums[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
# After adding -4 to nums[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
# After adding 2 to nums[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.
#
# Example 2:
# Input: nums = [1], queries = [[4,0]]
# Output: [0]

print(Solution().sumEvenAfterQueries(_nums, _queries))

print("--- %s seconds ---" % (time() - start_time))
