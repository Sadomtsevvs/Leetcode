from time import time


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        result = 0
        if len(nums) < 3:
            return result
        slices = [0, 0]
        delta = 1
        for i in range(2, len(nums)):
            slices.append(slices[i-1] + delta)
            delta += 1
        last_delta = nums[1] - nums[0]
        nums_in_row = 2
        for i in range(2, len(nums)):
            cur_delta = nums[i] - nums[i-1]
            if cur_delta == last_delta:
                nums_in_row += 1
            else:
                result += slices[nums_in_row - 1]
                nums_in_row = 2
                last_delta = cur_delta
        result += slices[nums_in_row - 1]
        return result

        # from LC comments
        #
        # dp = 0
        # total = 0
        # for i in range(2, len(nums)):
        #     if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
        #         dp += 1
        #         total += dp
        #     else:
        #         dp = 0
        # return total


start_time = time()

_nums = [1,2,4,6,5]
# Output: 3
# Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.

print(Solution().numberOfArithmeticSlices(_nums))

print("--- %s seconds ---" % (time() - start_time))
