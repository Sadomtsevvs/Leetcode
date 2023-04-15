from time import time
from typing import List


class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        result = []
        cur_max = 0
        cur_sum = 0
        for num in nums:
            cur_max = max(cur_max, num)
            cur_sum += (num + cur_max)
            result.append(cur_sum)
        return result


start_time = time()

# Example 1:
# Input: nums = [2,3,7,5,10]
# Output: [4,10,24,36,56]
_nums = [2,3,7,5,10]
# Explanation:
# For the prefix [2], the conversion array is [4] hence the score is 4
# For the prefix [2, 3], the conversion array is [4, 6] hence the score is 10
# For the prefix [2, 3, 7], the conversion array is [4, 6, 14] hence the score is 24
# For the prefix [2, 3, 7, 5], the conversion array is [4, 6, 14, 12] hence the score is 36
# For the prefix [2, 3, 7, 5, 10], the conversion array is [4, 6, 14, 12, 20] hence the score is 56
#
# Example 2:
# Input: nums = [1,1,2,4,8,16]
# Output: [2,4,8,16,32,64]
# Explanation:
# For the prefix [1], the conversion array is [2] hence the score is 2
# For the prefix [1, 1], the conversion array is [2, 2] hence the score is 4
# For the prefix [1, 1, 2], the conversion array is [2, 2, 4] hence the score is 8
# For the prefix [1, 1, 2, 4], the conversion array is [2, 2, 4, 8] hence the score is 16
# For the prefix [1, 1, 2, 4, 8], the conversion array is [2, 2, 4, 8, 16] hence the score is 32
# For the prefix [1, 1, 2, 4, 8, 16], the conversion array is [2, 2, 4, 8, 16, 32] hence the score is 64

print(Solution().findPrefixScore(_grid))

print("--- %s seconds ---" % (time() - start_time))
