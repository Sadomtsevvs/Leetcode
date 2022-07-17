from time import time
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        # let's implement a bottom up merge sort algorithm
        def merge(list1, list2):
            result = []
            p1, p2 = 0, 0
            while p1 < len(list1) and p2 < len(list2):
                if list1[p1] < list2[p2]:
                    result.append(list1[p1])
                    p1 += 1
                else:
                    result.append(list2[p2])
                    p2 += 1
            for i in range(p1, len(list1)):
                result.append(list1[i])
            for i in range(p2, len(list2)):
                result.append(list2[i])
            return result

        intervals = [[num] for num in nums]
        while len(intervals) > 1:
            next = []
            for i in range((len(intervals) + 1) // 2):
                if i * 2 == len(intervals) - 1:
                    next.append(intervals[2*i])
                else:
                    next.append(merge(intervals[2*i], intervals[2*i+1]))
            intervals = next
        return intervals[0]


start_time = time()

_nums = [5,1,1,2,0,0]
# Example 1:
# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
#
# Example 2:
# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]

print(Solution().sortArray(_nums))

print("--- %s seconds ---" % (time() - start_time))
