from time import time
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        for i in range(min(map(len, strs))):
            symb = ''
            for s in strs:
                if symb == '':
                    symb = s[i]
                elif s[i] != symb:
                    return ans
            ans += symb
        return ans



start_time = time()

_strs = ["flower","flow","flight"]
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

print(Solution().longestCommonPrefix(_strs))

print("--- %s seconds ---" % (time() - start_time))