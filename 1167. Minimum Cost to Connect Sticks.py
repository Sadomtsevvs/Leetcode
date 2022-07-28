import heapq
from time import time
from typing import List


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        answer = 0
        heapq.heapify(sticks)
        while len(sticks) > 1:
            stick = heapq.heappop(sticks) + heapq.heappop(sticks)
            answer += stick
            heapq.heappush(sticks, stick)
        return answer


start_time = time()

_sticks = [2,4,3]
# Example 1:
#
# Input: sticks = [2,4,3]
# Output: 14
# Explanation: You start with sticks = [2,4,3].
# 1. Combine sticks 2 and 3 for a cost of 2 + 3 = 5. Now you have sticks = [5,4].
# 2. Combine sticks 5 and 4 for a cost of 5 + 4 = 9. Now you have sticks = [9].
# There is only one stick left, so you are done. The total cost is 5 + 9 = 14.

# Example 2:
#
# Input: sticks = [1,8,3,5]
# Output: 30
# Explanation: You start with sticks = [1,8,3,5].
# 1. Combine sticks 1 and 3 for a cost of 1 + 3 = 4. Now you have sticks = [4,8,5].
# 2. Combine sticks 4 and 5 for a cost of 4 + 5 = 9. Now you have sticks = [9,8].
# 3. Combine sticks 9 and 8 for a cost of 9 + 8 = 17. Now you have sticks = [17].
# There is only one stick left, so you are done. The total cost is 4 + 9 + 17 = 30.

print(Solution().connectSticks(_sticks))

print("--- %s seconds ---" % (time() - start_time))
