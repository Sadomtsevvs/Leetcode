from time import time


class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        min, mid = float('inf'), float('inf')
        for num in nums:
            if num > mid:
                return True
            if num < min:
                min = num
            elif min < num < mid:
                mid = num
        return False


start_time = time()


_nums = [2,1,5,0,4,6]
_nums = [7,5,8,3,4,5]
_nums = [1,1,-2,6]
# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

print(Solution().increasingTriplet(_nums))

print("--- %s seconds ---" % (time() - start_time))
