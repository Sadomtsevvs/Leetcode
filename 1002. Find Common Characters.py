from time import time
from collections import Counter


class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        cntr_words = [Counter(word) for word in words]
        cntr = cntr_words[0]
        for char in cntr:
            for cntr_word in cntr_words:
                cntr[char] = min(cntr[char], cntr_word[char])
        return [char for char, val in cntr.items() for _ in range(val)]

        # solution from Lee
        #
        # res = Counter(words[0])
        # for a in words:
        #     res &= Counter(a)
        # return list(res.elements())


start_time = time()

_words = ["bella","label","roller"]
# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]

print(Solution().commonChars(_words))

print("--- %s seconds ---" % (time() - start_time))
