from time import time
from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        from_left = [0 for _ in range(len(seats))]
        from_right = [0 for _ in range(len(seats))]
        left, right = float('inf'), float('inf')
        for i in range(len(seats)):
            if seats[i] == 1:
                left = 1
            else:
                from_left[i] = left
                left += 1
            if seats[-i-1] == 1:
                right = 1
            else:
                from_right[-i-1] = right
                right += 1
        result = 1
        for i in range(len(seats)):
            result = max(result, min(from_left[i], from_right[i]))
        return result


start_time = time()

_seats = [1,0,0,0,1,0,1]
# Example 1:
# Input: seats = [1,0,0,0,1,0,1]
# Output: 2
# Explanation:
# If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
# If Alex sits in any other open seat, the closest person has distance 1.
# Thus, the maximum distance to the closest person is 2.
#
# Example 2:
# Input: seats = [1,0,0,0]
# Output: 3
# Explanation:
# If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
# This is the maximum distance possible, so the answer is 3.
#
# Example 3:
# Input: seats = [0,1]
# Output: 1

print(Solution().maxDistToClosest(_seats))

print("--- %s seconds ---" % (time() - start_time))
