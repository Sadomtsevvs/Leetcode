from time import time
from collections import defaultdict


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        sequences = defaultdict(int)
        for i in range(len(s) - 9):
            sequences[s[i:i+10]] += 1
        return [key for key, value in sequences.items() if value > 1]


start_time = time()

_s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
_s = "AAAAAAAAAAA"
# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]

print(Solution().findRepeatedDnaSequences(_s))

print("--- %s seconds ---" % (time() - start_time))
