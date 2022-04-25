from time import time
from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:

        # solution from LC comments, fast

        sub = []
        for num in nums:
            i = bisect_left(sub, num)
            if i == len(sub):
                sub.append(num)
            else:
                sub[i] = num
        return len(sub)

        # my solution, rather slow
        #
        # result = [1] * len(nums)
        # for i in range(1, len(nums)):
        #     result[i] = max([0] + [result[j] for j in range(i - 1, -1, -1) if nums[j] < nums[i]]) + 1
        # return max(result)


start_time = time()

# _nums = [1,3,6,7,9,4,10,5,6]
_nums = [10,9,2,5,3,7,101,18]
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

print(Solution().lengthOfLIS(_nums))

print("--- %s seconds ---" % (time() - start_time))
