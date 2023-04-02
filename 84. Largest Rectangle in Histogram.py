from time import time
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        # brute-force, TLE, O(n**2)
        # result = 0
        # for i in range(len(heights)):
        #     min_height = heights[i]
        #     for j in range(i, len(heights)):
        #         min_height = min(min_height, heights[j])
        #         result = max(result, (j - i + 1) * min_height)
        # return result

        # little optimized but still O(n**2)
        # result = 0
        # for i in range(len(heights)):
        #     min_height = heights[i]
        #     if i > 0 and heights[i-1] >= min_height:
        #         continue
        #     for j in range(i, len(heights)):
        #         min_height = min(min_height, heights[j])
        #         result = max(result, (j - i + 1) * min_height)
        # return result

        # after reading community submissions
        result = 0
        heights.append(0)
        stack = [-1]
        for i in range(len(heights)):
            while heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                result = max(result, h * w)
            stack.append(i)
        return result


start_time = time()

# Example 1:
_heights = [2,1,5,6,2,3]
# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.
#
# Example 2:
# Input: heights = [2,4]
# Output: 4
# _heights = [2,4]


print(Solution().largestRectangleArea(_heights))

print("--- %s seconds ---" % (time() - start_time))
