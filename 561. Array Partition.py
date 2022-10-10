from time import time
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # my first heap solution
        #
        # result = 0
        # heapq.heapify(nums)
        # while nums:
        #     result += heapq.heappop(nums)
        #     heapq.heappop(nums)
        # return result

        result = 0
        nums.sort()
        for i in range(0, len(nums), 2):
            result += nums[i]
        return result

        # official solution
        #
        # K = 10000
        # # Store the frequency of each element
        # element_to_count = [0] * (2 * K + 1)
        # for element in nums:
        #     # Add K to element to offset negative values
        #     element_to_count[element + K] += 1
        #
        # # Initialize sum to zero
        # max_sum = 0
        # is_even_index = True
        # for element in range(2 * K + 1):
        #     while element_to_count[element] > 0:
        #         # Add element if it is at even index
        #         if is_even_index:
        #             max_sum += element - K
        #         # Flip the value (one to zero or zero to one)
        #         is_even_index = not is_even_index;
        #         # Decrement the frequency count
        #         element_to_count[element] -= 1
        # return max_sum

        # from LC, 1-liner
        #
        # return sum(sorted(nums)[::2])


start_time = time()

# Example 1:
# Input: nums = [1,4,3,2]
# Output: 4
# Explanation: All possible pairings (ignoring the ordering of elements) are:
# 1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
# 2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
# 3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
# So the maximum possible sum is 4.
#
_nums = [6,2,6,5,1,2]
# Example 2:
# Input: nums = [6,2,6,5,1,2]
# Output: 9
# Explanation: The optimal pairing is (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9.

print(Solution().arrayPairSum(_nums))

print("--- %s seconds ---" % (time() - start_time))
