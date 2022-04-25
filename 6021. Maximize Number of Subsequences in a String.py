from time import time
from collections import Counter


class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        cntr = Counter(text)
        if pattern[0] == pattern[1]:
            exist0 = cntr[pattern[0]]
            return (exist0 + 1) * exist0 // 2
        else:
            non_orders = 0
            count1 = 0
            for t in text:
                if t == pattern[0]:
                    non_orders += count1
                elif t == pattern[1]:
                    count1 += 1
            exist0 = cntr[pattern[0]]
            exist1 = cntr[pattern[1]]
            return max((exist0 + 1)*exist1, exist0*(exist1+1)) - non_orders


start_time = time()

_text = "abdcdbc"
_pattern = "ac"
_text = "aabb"
_pattern = "ab"
# _text = "aaaabb"
# _pattern = "aa"

# _text = "mpmp"
# _text = "iekbksdsmuuzwxbpmcngsfkjvpzuknqguzvzik"
# _pattern = "mp"
# Output:6
# Expected:5

# Input: text = "abdcdbc", pattern = "ac"
# Output: 4
# Explanation:
# If we add pattern[0] = 'a' in between text[1] and text[2], we get "abadcdbc". Now, the number of times "ac" occurs as a subsequence is 4.
# Some other strings which have 4 subsequences "ac" after adding a character to text are "aabdcdbc" and "abdacdbc".
# However, strings such as "abdcadbc", "abdccdbc", and "abdcdbcc", although obtainable, have only 3 subsequences "ac" and are thus suboptimal.
# It can be shown that it is not possible to get more than 4 subsequences "ac" by adding only one character.

print(Solution().maximumSubsequenceCount(_text, _pattern))

print("--- %s seconds ---" % (time() - start_time))