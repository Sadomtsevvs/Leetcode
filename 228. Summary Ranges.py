from time import time
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        if not nums:
            return result
        beg = -1
        prev = -1
        for num in nums:
            if beg == -1:
                beg = num
            elif prev + 1 < num:
                if beg == prev:
                    result.append(str(beg))
                else:
                    result.append(str(beg) + "->" + str(prev))
                beg = num
            prev = num
        if beg == prev:
            result.append(str(beg))
        else:
            result.append(str(beg) + "->" + str(prev))
        return result


start_time = time()

# Example 1:
# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"
#
# Example 2:
# Input: nums = [0,2,3,4,6,8,9]
_nums = [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: The ranges are:
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"

_nums = []

print(Solution().summaryRanges(_nums))

print("--- %s seconds ---" % (time() - start_time))
