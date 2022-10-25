from time import time
from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:

        def s_to_bin(string):
            num = 0
            for char in string:
                digit = ord(char) - 96
                num |= (1 << digit)
            return num

        words = []

        for s in arr:
            len_s = len(s)
            if len_s > len(set(s)):
                continue
            words.append((s_to_bin(s), len_s))

        result = [0]

        def dfs(cur_num, cur_length, ind):
            for i in range(ind, len(words)):
                num, length = words[i]
                if cur_num & num != 0:
                    continue
                result[0] = max(result[0], cur_length + length)
                dfs(cur_num | num, cur_length + length, i + 1)

        dfs(0, 0, 0)

        return result[0]


start_time = time()

_arr = ["un","iq","ue"]
# Example 1:
# Input: arr = ["un","iq","ue"]
# Output: 4
# Explanation: All the valid concatenations are:
# - ""
# - "un"
# - "iq"
# - "ue"
# - "uniq" ("un" + "iq")
# - "ique" ("iq" + "ue")
# Maximum length is 4.
#
_arr = ["cha","r","act","ers"]
# Example 2:
# Input: arr = ["cha","r","act","ers"]
# Output: 6
# Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").
#
# Example 3:
# Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
# Output: 26
# Explanation: The only string in arr has all 26 characters.
# _arr = ["aa","bb"]
_arr = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]

print(Solution().maxLength(_arr))

print("--- %s seconds ---" % (time() - start_time))
