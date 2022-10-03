from time import time
from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        result = 0
        prev_col = '!'
        min_time = 0
        for i, color in enumerate(colors):
            cur_time = neededTime[i]
            if color == prev_col:
                if cur_time < min_time:
                    result += cur_time
                else:
                    result += min_time
                    min_time = cur_time
            else:
                prev_col = color
                min_time = cur_time
        return result


start_time = time()

# Example 1:
# Input: colors = "abaac", neededTime = [1,2,3,4,5]
# Output: 3
# Explanation: In the above image, 'a' is blue, 'b' is red, and 'c' is green.
# Bob can remove the blue balloon at index 2. This takes 3 seconds.
# There are no longer two consecutive balloons of the same color. Total time = 3.
#
# Example 2:
# Input: colors = "abc", neededTime = [1,2,3]
# Output: 0
# Explanation: The rope is already colorful. Bob does not need to remove any balloons from the rope.
#
_colors = "aabaa"
_neededTime = [1,2,3,4,1]
# Example 3:
# Input: colors = "aabaa", neededTime = [1,2,3,4,1]
# Output: 2
# Explanation: Bob will remove the ballons at indices 0 and 4. Each ballon takes 1 second to remove.
# There are no longer two consecutive balloons of the same color. Total time = 1 + 1 = 2.

print(Solution().minCost(_colors, _neededTime))

print("--- %s seconds ---" % (time() - start_time))
