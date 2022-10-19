import heapq
from collections import Counter
from time import time
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cntr = Counter(words)
        heap = [(-val, key) for key, val in cntr.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]


start_time = time()

_words = ["i","love","leetcode","i","love","coding"]
_k = 2
# Example 1:
# Input: words = ["i","love","leetcode","i","love","coding"], k = 2
# Output: ["i","love"]
# Explanation: "i" and "love" are the two most frequent words.
# Note that "i" comes before "love" due to a lower alphabetical order.
#
# Example 2:
# Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
# Output: ["the","is","sunny","day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.

print(Solution().topKFrequent(_words, _k))

print("--- %s seconds ---" % (time() - start_time))
