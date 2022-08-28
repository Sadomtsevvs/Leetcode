from time import time
from collections import defaultdict, Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        return Counter(ransomNote) <= Counter(magazine)

        # my first solution
        #
        # if len(ransomNote) > len(magazine):
        #     return False
        # dict_note = defaultdict(int)
        # dict_magazine = defaultdict(int)
        # for s in ransomNote:
        #     dict_note[s] += 1
        # for s in magazine:
        #     dict_magazine[s] += 1
        # for key, value in dict_note.items():
        #     if value > dict_magazine[key]:
        #         return False
        # return True


start_time = time()

_ransomNote = "aa"
_magazine = "ab"
# Input: ransomNote = "aa", magazine = "aab"
# Output: true

print(Solution().canConstruct(_ransomNote, _magazine))

print("--- %s seconds ---" % (time() - start_time))