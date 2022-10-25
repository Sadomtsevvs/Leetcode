from time import time
from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)


start_time = time()

_word1 = ["ab", "c"]
_word2 = ["a", "bc"]
# Example 1:
# Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
# Output: true
# Explanation:
# word1 represents string "ab" + "c" -> "abc"
# word2 represents string "a" + "bc" -> "abc"
# The strings are the same, so return true.
#
# Example 2:
# Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
# Output: false
#
# Example 3:
# Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
# Output: true

print(Solution().arrayStringsAreEqual(_word1, _word2))

print("--- %s seconds ---" % (time() - start_time))
