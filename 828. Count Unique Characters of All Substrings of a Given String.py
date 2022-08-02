from time import time


class Solution:
    def uniqueLetterString(self, s: str) -> int:

        result = 1
        prev_row = 1
        dic = {s[0]: (-1, 0)}
        for i in range(1, len(s)):
            char = s[i]
            if char in dic:
                row = prev_row + i - 2 * dic[char][1] + dic[char][0]
                dic[char] = (dic[char][1], i)
            else:
                row = prev_row + i + 1
                dic[char] = (-1, i)
            result += row
            prev_row = row
        return result

        # my first solution
        #
        # result = 1
        # prev_row = 1
        # dic = {s[0]: (-1, 0)}
        # for i in range(1, len(s)):
        #     if s[i] in dic:
        #         row = prev_row - (dic[s[i]][1] - dic[s[i]][0]) + (i - dic[s[i]][1])
        #         dic[s[i]] = (dic[s[i]][1], i)
        #     else:
        #         row = prev_row + (i + 1)
        #         dic[s[i]] = (-1, i)
        #     result += row
        #     prev_row = row
        # return result


start_time = time()

_s = "ABC"
# Example 1:
# Input: s = "ABC"
# Output: 10
# Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
# Every substring is composed with only unique letters.
# Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10
#
_s = "ABA"
# Example 2:
# Input: s = "ABA"
# Output: 8
# Explanation: The same as example 1, except countUniqueChars("ABA") = 1.
#
_s = "LEETCODE"
# Example 3:
# Input: s = "LEETCODE"
# Output: 92

print(Solution().uniqueLetterString(_s))

print("--- %s seconds ---" % (time() - start_time))
