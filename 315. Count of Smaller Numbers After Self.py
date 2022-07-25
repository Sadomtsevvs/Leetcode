from bisect import bisect_left
from time import time
from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # wrong answer
        #
        # result = []
        # mx = nums[0]
        # max_ind = 0
        # for i in range(len(nums)):
        #     if i > 0 and nums[i] >= mx:
        #         result.append(result[max_ind] - (i - max_ind - 1))
        #         mx = nums[i]
        #         max_ind = i
        #         continue
        #     cnt = 0
        #     for j in range(i+1, len(nums)):
        #         if nums[j] < nums[i]:
        #             cnt += 1
        #     result.append(cnt)
        # return result

        # from LC
        #
        sorted_arr = []
        rst = []
        for num in nums[::-1]:
            idx = bisect_left(sorted_arr, num)
            rst.append(idx)
            sorted_arr.insert(idx, num)
        return rst[::-1]


start_time = time()

_nums = [5,2,6,1]
# Input: nums = [5,2,6,1]
# Output: [2,1,1,0]
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.

_nums = [-1,-1]

print(Solution().countSmaller(_nums))

print("--- %s seconds ---" % (time() - start_time))
