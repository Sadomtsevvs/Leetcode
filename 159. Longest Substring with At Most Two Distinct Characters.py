from time import time


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        res = 1
        first, second, last = None, None, None
        first_ind, second_ind, last_ind = float('inf'), float('inf'), float('inf')
        for i, char in enumerate(s):
            if not first:
                first = char
                first_ind = i
                last = first
                last_ind = i
            elif not second and char != first:
                second = char
                last = second
                last_ind = i
            elif char != first and char != second:
                first, second, last = last, char, char
                first_ind, last_ind = last_ind, i
            elif char == first and second:
                first, second, last = second, first, char
                last_ind = i
            res = max(res, i - first_ind + 1)
        return res



start_time = time()

_paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]

_s = "eceba"
# Example 1:
# Input: s = "eceba"
# Output: 3
# Explanation: The substring is "ece" which its length is 3.
#
_s = "ccaabbb"
# Example 2:
# Input: s = "ccaabbb"
# Output: 5
# Explanation: The substring is "aabbb" which its length is 5.

print(Solution().lengthOfLongestSubstringTwoDistinct(_s))

print("--- %s seconds ---" % (time() - start_time))
