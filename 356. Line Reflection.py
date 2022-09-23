from collections import defaultdict
from time import time
from typing import List


class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        dic = defaultdict(set)
        for x, y in points:
            dic[y].add(x)
        for y, xs in dic.items():
            dic[y] = sorted(list(xs))
        common_line = None
        for xs in dic.values():
            left, right = 0, len(xs) - 1
            while left <= right:
                if xs[left] == xs[right]:
                    cur_line = xs[left]
                else:
                    cur_line = (xs[right] + xs[left]) / 2
                if not common_line:
                    common_line = cur_line
                elif cur_line != common_line:
                    return False
                left += 1
                right -= 1
        return True

        # solution from LC comments
        #
        # if not points:
        #     return True  # very weird, but this is the expected answer of the OJ...
        # points = set([tuple(p) for p in points])
        # mid = (min(x for x, y in points) + max(x for x, y in points)) / 2
        #
        # for x, y in points:
        #     mirror_x = mid + (mid - x)
        #     if (mirror_x, y) not in points:
        #         return False
        #
        # return True


start_time = time()

_nums = [1,2,3,4]
_queries = [[1,0],[-3,1],[-4,0],[2,3]]
# Example 1:
# Input: nums = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
# Output: [8,6,2,4]
# Explanation: At the beginning, the array is [1,2,3,4].
# After adding 1 to nums[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
# After adding -3 to nums[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
# After adding -4 to nums[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
# After adding 2 to nums[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.
#
# Example 2:
# Input: nums = [1], queries = [[4,0]]
# Output: [0]

print(Solution().sumEvenAfterQueries(_nums, _queries))

print("--- %s seconds ---" % (time() - start_time))
