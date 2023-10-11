from time import time
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        # nums = set(nums)
        # num = 1
        # while True:
        #     if num not in nums:
        #         return num
        #     num += 1

        # from comments
        #
        """
        :type nums: List[int]
        :rtype: int
         Basic idea:
        1. for any array whose length is l, the first missing positive must be in range [1,...,l+1],
            so we only have to care about those elements in this range and remove the rest.
        2. we can use the array index as the hash to restore the frequency of each number within
             the range [1,...,l+1]
        """
        nums.append(0)
        n = len(nums)
        for i in range(len(nums)):  # delete those useless elements
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        for i in range(len(nums)):  # use the index as the hash to record the frequency of each number
            nums[nums[i] % n] += n
        for i in range(1, len(nums)):
            if nums[i] // n == 0:
                return i
        return n


start_time = time()

# Example 1:
# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.
#
# Example 2:
# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.
#
# Example 3:
# Input: nums = [7,8,9,11,12]
_nums = [2,4,3,9,11]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.

print(Solution().firstMissingPositive(_nums))

print("--- %s seconds ---" % (time() - start_time))
