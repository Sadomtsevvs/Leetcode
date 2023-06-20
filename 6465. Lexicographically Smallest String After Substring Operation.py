from time import time


class Solution:
    def smallestString(self, s: str) -> str:

        beg, end = -1, -1
        for i in range(len(s)):
            if beg == -1 and s[i] != 'a':
                beg = i
            if s[i] != 'a':
                end = i
            elif end != -1:
                break
        if beg == -1 and end == -1:
            beg, end = len(s) - 1, len(s) - 1
        arr = list(s)
        for i in range(beg, end + 1):
            if arr[i] == 'a':
                arr[i] = 'z'
            else:
                arr[i] = chr(ord(arr[i])-1)
        return ''.join(arr)


start_time = time()

# Example 1:
# Input: s = "cbabc"
_s = "cbabc"
# Output: "baabc"
# Explanation: We apply the operation on the substring starting at index 0, and ending at index 1 inclusive.
# It can be proven that the resulting string is the lexicographically smallest.
#
# Example 2:
# Input: s = "acbbc"
# _s = "acbbc"
# Output: "abaab"
# Explanation: We apply the operation on the substring starting at index 1, and ending at index 4 inclusive.
# It can be proven that the resulting string is the lexicographically smallest.
#
# Example 3:
# Input: s = "leetcode"
# _s = "leetcode"
# Output: "kddsbncd"
# Explanation: We apply the operation on the entire string.
# It can be proven that the resulting string is the lexicographically smallest.

# _s = 'aaa'

print(Solution().smallestString(_s))

print("--- %s seconds ---" % (time() - start_time))
