from time import time
from typing import List


class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:

        result = []

        n = len(words[0])

        trie = {'': ({}, [])}
        for word in words:
            node = trie
            for char in word:
                if char not in node:
                    node[char] = ({}, [word])
                else:
                    node[char][1].append(word)
                node = node[char][0]

        def backtrack(i, cur):
            if i == n:
                result.append(cur)
                return
            node = trie
            for word in cur:
                if word[i] not in node:
                    return
                words = node[word[i]][1]
                node = node[word[i]][0]
            for word in words:
                backtrack(i + 1, cur + [word])

        for word in words:
            backtrack(1, [word])

        return result


start_time = time()

_words = ["area","lead","wall","lady","ball"]
# Example 1:
# Input: words = ["area","lead","wall","lady","ball"]
# Output: [["ball","area","lead","lady"],["wall","area","lead","lady"]]
# Explanation:
# The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
#
# Example 2:
# Input: words = ["abat","baba","atan","atal"]
# Output: [["baba","abat","baba","atal"],["baba","abat","baba","atan"]]
# Explanation:
# The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).

print(Solution().wordSquares(_words))

print("--- %s seconds ---" % (time() - start_time))
