from time import time


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        i = 0
        len1, len2 = len(word1), len(word2)
        while True:
            if i == len1:
                result += word2[i:]
                break
            if i == len2:
                result += word1[i:]
                break
            result += word1[i] + word2[i]
            i += 1
        return result

        # from LC comments
        #
        # return ''.join(a + b for a, b in zip_longest(w1, w2, fillvalue=''))


start_time = time()

_word1 = "abc"
_word2 = "pqroooo"
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r

print(Solution().mergeAlternately(_word1, _word2))

print("--- %s seconds ---" % (time() - start_time))
