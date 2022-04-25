from time import time


class Solution:
    def smallestDistancePair(self, nums: list[int], k: int) -> int:

        nums.sort()

        def num_of_pairs_less_equal_than_x(x: int) -> int:
            result = 0
            first, second = 0, 1
            while True:
                while second != len(nums) and nums[second] - nums[first] <= x:
                    second += 1
                n = second - first
                result += (n * (n - 1)) // 2
                if second == len(nums):
                    break
                while nums[second] - nums[first] > x:
                    first += 1
                n = second - first
                result -= (n * (n - 1)) // 2
            return result

        beg, end = 0, nums[-1] - nums[0]
        while beg < end:
            mid = (beg + end) // 2
            if num_of_pairs_less_equal_than_x(mid) >= k:
                end = mid
            else:
                beg = mid + 1

        return beg


start_time = time()

_nums = [1,3,1]
_k = 4
_nums = [1,1,1]
_k = 3
# Input: nums = [1,3,1], k = 1
# Output: 0
# Explanation: Here are all the pairs:
# (1,3) -> 2
# (1,1) -> 0
# (3,1) -> 2
# Then the 1st smallest distance pair is (1,1), and its distance is 0.

print(Solution().smallestDistancePair(_nums, _k))

print("--- %s seconds ---" % (time() - start_time))