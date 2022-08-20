from time import time
from typing import List


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # time O(n**2)
        stack = []
        for num in nums:
            for i in range(len(stack)):
                st = stack[-i-1]
                if st[-1] == num - 1:
                    st.append(num)
                    break
                if len(st) < 3 and st[-1] < num - 1:
                    return False
            else:
                stack.append([num])
        for st in stack:
            if len(st) < 3:
                return False
        return True

        # Lee solution
        #
        # left = collections.Counter(nums)
        # end = collections.Counter()
        # for num in nums:
        #     if not left[num]: continue
        #     left[num] -= 1
        #     if end[num - 1] > 0:
        #         end[num - 1] -= 1
        #         end[num] += 1
        #     elif left[num + 1] and left[num + 2]:
        #         left[num + 1] -= 1
        #         left[num + 2] -= 1
        #         end[num + 2] += 1
        #     else:
        #         return False
        # return True


start_time = time()

_nums = [1,2,3,3,4,5]
# Example 1:
# Input: nums = [1,2,3,3,4,5]
# Output: true
# Explanation: nums can be split into the following subsequences:
# [1,2,3,3,4,5] --> 1, 2, 3
# [1,2,3,3,4,5] --> 3, 4, 5
#
_nums = [1,2,3,3,4,4,5,5]
# Example 2:
# Input: nums = [1,2,3,3,4,4,5,5]
# Output: true
# Explanation: nums can be split into the following subsequences:
# [1,2,3,3,4,4,5,5] --> 1, 2, 3, 4, 5
# [1,2,3,3,4,4,5,5] --> 3, 4, 5
#
# Example 3:
# Input: nums = [1,2,3,4,4,5]
# Output: false
# Explanation: It is impossible to split nums into consecutive increasing subsequences of length 3 or more.

print(Solution().isPossible(_nums))

print("--- %s seconds ---" % (time() - start_time))
