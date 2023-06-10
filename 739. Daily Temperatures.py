from time import time
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)-1, -1, -1):
            temp = temperatures[i]
            while stack and temperatures[stack[-1]] <= temp:
                stack.pop()
            if stack:
                result[i] = stack[-1] - i
            else:
                result[i] = 0
            stack.append(i)
        return result


start_time = time()

# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i]
# is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day
# for which this is possible, keep answer[i] == 0 instead.

# Example 1:
# Input: temperatures = [73,74,75,71,69,72,76,73]
_temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
#
# Example 2:
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
#
# Example 3:
# Input: temperatures = [30,60,90]
# Output: [1,1,0]


print(Solution().dailyTemperatures(_temperatures))

print("--- %s seconds ---" % (time() - start_time))
