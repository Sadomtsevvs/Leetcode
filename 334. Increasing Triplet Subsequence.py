from time import time


class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        # my second solution. complicated
        #
        first, second = None, None
        for num in nums:
            if second is not None and num > second:
                return True
            if first is None:
                first = num
            elif num < first:
                first = num
            elif num > first:
                if second is None:
                    second = num
                elif num < second:
                    second = num
        return False

        # min, mid = float('inf'), float('inf')
        # for num in nums:
        #     if num > mid:
        #         return True
        #     if num < min:
        #         min = num
        #     elif min < num < mid:
        #         mid = num
        # return False


start_time = time()


_nums = [2,1,5,0,4,6]
_nums = [7,5,8,3,4,5]
_nums = [1,1,-2,6]
_nums = [1,0,0,-1,0,0,1000]
# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

print(Solution().increasingTriplet(_nums))

print("--- %s seconds ---" % (time() - start_time))
