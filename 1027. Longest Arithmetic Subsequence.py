from collections import defaultdict
from time import time
from typing import List


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        ans = 2
        subs = defaultdict(dict)
        for i in range(1, len(nums)):
            num = nums[i]
            seen = set()
            for j in range(i - 1, -1, -1):
                diff = num - nums[j]
                if diff in seen:
                    continue
                if diff in subs[j]:
                    subs[i][diff] = subs[j][diff] + 1
                else:
                    subs[i][diff] = 2
                seen.add(diff)
                ans = max(ans, subs[i][diff])
        return ans


start_time = time()

# Example 1:
# Input: nums = [3,6,9,12]
_nums = [3,6,9,12]
# Output: 4
# Explanation:  The whole array is an arithmetic sequence with steps of length = 3.
#
# Example 2:
# Input: nums = [9,4,7,2,10]
_nums = [9,4,7,2,10]
# Output: 3
# Explanation:  The longest arithmetic subsequence is [4,7,10].
#
# Example 3:
# Input: nums = [20,1,15,3,10,5,8]
_nums = [20,1,15,3,10,5,8]
# Output: 4
# Explanation:  The longest arithmetic subsequence is [20,15,10,5].

print(Solution().longestArithSeqLength(_nums))

print("--- %s seconds ---" % (time() - start_time))
