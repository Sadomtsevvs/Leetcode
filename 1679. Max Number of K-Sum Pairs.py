from time import time
from typing import List
from collections import defaultdict


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        d = defaultdict(int)
        for num in nums:
            target = k - num
            if d[target] > 0:
                d[target] -= 1
                ans += 1
            else:
                d[num] += 1
        return ans

        # solution from Babichev
        #
        # cnt, ans = Counter(nums), 0
        # for val in cnt:
        #     ans += min(cnt[val], cnt[k - val])
        # return ans//2

start_time = time()

_nums = [1,2,3,4]
_k = 5
# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.

print(Solution().maxOperations(_nums, _k))

print("--- %s seconds ---" % (time() - start_time))
