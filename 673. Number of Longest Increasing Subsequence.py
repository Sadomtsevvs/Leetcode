from time import time


# from bisect import bisect_left


class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        # solution from LC comment
        #
        # dp, longest = [[1, 1] for i in range(len(nums))], 1
        # for i, num in enumerate(nums):
        #     curr_longest, count = 1, 0
        #     for j in range(i):
        #         if nums[j] < num:
        #             curr_longest = max(curr_longest, dp[j][0] + 1)
        #     for j in range(i):
        #         if dp[j][0] == curr_longest - 1 and nums[j] < num:
        #             count += dp[j][1]
        #     dp[i] = [curr_longest, max(count, dp[i][1])]
        #     longest = max(curr_longest, longest)
        # return sum([item[1] for item in dp if item[0] == longest])

        # after reading the above comment
        cur_longest = [1] * len(nums)
        number_longest = [1] * len(nums)
        for i in range(1, len(nums)):
            cur_longest[i] = max([0] + [cur_longest[j] for j in range(i - 1, -1, -1) if nums[j] < nums[i]]) + 1
            number_longest[i] = max(1, sum([number_longest[j] for j in range(i - 1, -1, -1) if nums[j] < nums[i] and
                                            cur_longest[j] == cur_longest[i] - 1]))
        return sum([number_longest[i] for i in range(len(nums)) if cur_longest[i] == max(cur_longest)])


start_time = time()

_nums = [0, 1, 0, 1, 3, 2, 3]
# _nums = [0,1,0,1,3,2,3]
# _nums = [1,3,5,4,7]
# Input: nums = [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
#
# Input: nums = [2,2,2,2,2]
# Output: 5
# Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.

print(Solution().findNumberOfLIS(_nums))

print("--- %s seconds ---" % (time() - start_time))
