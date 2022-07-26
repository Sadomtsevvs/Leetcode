from time import time
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        # solution after reading official
        #
        answer = 0
        left, right = 0, 0
        zeros = 0
        while right < len(nums):
            if nums[right] == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            answer = max(answer, right - left + 1)
            right += 1

        return answer

        # my first solution, too complex
        #
        # result = 0
        # first_ones = 0
        # second_ones = 0
        # first_group = True
        # prev = 1
        # for num in nums:
        #     if num == 1:
        #         if first_group:
        #             first_ones += 1
        #         else:
        #             second_ones += 1
        #     elif prev == 0:
        #         result = max(result, first_ones + second_ones + 1)
        #         first_ones = 0
        #         second_ones = 0
        #         first_group = True
        #     else:
        #         if first_group and first_ones > 0:
        #             first_group = False
        #         else:
        #             result = max(result, first_ones + second_ones + 1)
        #             first_ones = second_ones
        #             second_ones = 0
        #     prev = num
        # return max(result, min(first_ones + second_ones + 1, len(nums)))

        # from LC, great
        #
        # # previous and current length of consecutive 1
        # pre, curr, maxlen = -1, 0, 0
        # for n in nums:
        #     if n == 0:
        #         pre, curr = curr, 0
        #     else:
        #         curr += 1
        #     maxlen = max(maxlen, pre + 1 + curr)
        # return maxlen


        # official solution, two pointers with sliding window
        #
        # longest_sequence = 0
        # left, right = 0, 0
        # num_zeroes = 0
        #
        # while right < len(nums):   # while our window is in bounds
        #     if nums[right] == 0:    # add the right most element into our window
        #         num_zeroes += 1
        #
        #     while num_zeroes == 2:   # if our window is invalid, contract our window
        #         if nums[left] == 0:
        #             num_zeroes -= 1
        #         left += 1
        #
        #     longest_sequence = max(longest_sequence, right - left + 1)   # update our longest sequence answer
        #     right += 1   # expand our window
        #
        # return longest_sequence


start_time = time()

_nums = [1,1,0,0,1,0,1,1]
# Input: nums = [1,0,1,1,0]
# Output: 4
# Explanation: Flip the first zero will get the maximum number of consecutive 1s.
# After flipping, the maximum number of consecutive 1s is 4.

print(Solution().findMaxConsecutiveOnes(_nums))

print("--- %s seconds ---" % (time() - start_time))
