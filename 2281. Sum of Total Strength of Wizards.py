from itertools import accumulate
from time import time
from typing import List


class Solution:
    def totalStrength(self, strength: List[int]) -> int:

        # Lee solution
        #
        mod = 10 ** 9 + 7
        n = len(strength)

        # next small index on the right
        right = [n] * n
        stack = []
        for i in range(n):
            while stack and strength[stack[-1]] > strength[i]:
                right[stack.pop()] = i
            stack.append(i)

        # next small index on the left
        left = [-1] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and strength[stack[-1]] >= strength[i]:
                left[stack.pop()] = i
            stack.append(i)

        # for each A[i] as minimum, calculate sum
        res = 0
        acc = list(accumulate(accumulate(strength), initial=0))
        for i in range(n):
            l, r = left[i], right[i]
            lacc = acc[i] - acc[max(l, 0)]
            racc = acc[r] - acc[i]
            ln, rn = i - l, r - i
            res += strength[i] * (racc * ln - lacc * rn)
        return res % mod




start_time = time()

_strength = [1, 3, 2, 4]
# Example 1:
# Input: strength = [1,3,1,2]
# Output: 44
# Explanation: The following are all the contiguous groups of wizards:
# - [1] from [1,3,1,2] has a total strength of min([1]) * sum([1]) = 1 * 1 = 1
# - [3] from [1,3,1,2] has a total strength of min([3]) * sum([3]) = 3 * 3 = 9
# - [1] from [1,3,1,2] has a total strength of min([1]) * sum([1]) = 1 * 1 = 1
# - [2] from [1,3,1,2] has a total strength of min([2]) * sum([2]) = 2 * 2 = 4
# - [1,3] from [1,3,1,2] has a total strength of min([1,3]) * sum([1,3]) = 1 * 4 = 4
# - [3,1] from [1,3,1,2] has a total strength of min([3,1]) * sum([3,1]) = 1 * 4 = 4
# - [1,2] from [1,3,1,2] has a total strength of min([1,2]) * sum([1,2]) = 1 * 3 = 3
# - [1,3,1] from [1,3,1,2] has a total strength of min([1,3,1]) * sum([1,3,1]) = 1 * 5 = 5
# - [3,1,2] from [1,3,1,2] has a total strength of min([3,1,2]) * sum([3,1,2]) = 1 * 6 = 6
# - [1,3,1,2] from [1,3,1,2] has a total strength of min([1,3,1,2]) * sum([1,3,1,2]) = 1 * 7 = 7
# The sum of all the total strengths is 1 + 9 + 1 + 4 + 4 + 4 + 3 + 5 + 6 + 7 = 44.
#
# Example 2:
# Input: strength = [5,4,6]
# Output: 213
# Explanation: The following are all the contiguous groups of wizards:
# - [5] from [5,4,6] has a total strength of min([5]) * sum([5]) = 5 * 5 = 25
# - [4] from [5,4,6] has a total strength of min([4]) * sum([4]) = 4 * 4 = 16
# - [6] from [5,4,6] has a total strength of min([6]) * sum([6]) = 6 * 6 = 36
# - [5,4] from [5,4,6] has a total strength of min([5,4]) * sum([5,4]) = 4 * 9 = 36
# - [4,6] from [5,4,6] has a total strength of min([4,6]) * sum([4,6]) = 4 * 10 = 40
# - [5,4,6] from [5,4,6] has a total strength of min([5,4,6]) * sum([5,4,6]) = 4 * 15 = 60
# The sum of all the total strengths is 25 + 16 + 36 + 36 + 40 + 60 = 213.

print(Solution().totalStrength(_strength))

print("--- %s seconds ---" % (time() - start_time))
