from time import time
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0]
        step_back = 1
        half = 1
        digits = 2
        for i in range(1, n + 1):
            if i == digits:
                step_back = digits//2
                half = digits + step_back
                digits *= 2
            if i < half:
                result.append(result[i-step_back])
            else:
                result.append(result[i-step_back] + 1)
        return result


start_time = time()

# Example 1:
# Input: n = 2
_n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
#
# Example 2:
# Input: n = 5
_n = 15
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101

print(Solution().countBits(_n))

print("--- %s seconds ---" % (time() - start_time))
