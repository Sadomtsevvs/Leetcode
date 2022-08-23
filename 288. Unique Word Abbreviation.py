from collections import defaultdict
from typing import List


class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.dic = defaultdict(set)
        for s in dictionary:
            abbr = s[0] + ("" if len(s) < 3 else str(len(s) - 2)) + s[-1]
            self.dic[abbr].add(s)

    def isUnique(self, word: str) -> bool:
        abbr = word[0] + ("" if len(word) < 3 else str(len(word) - 2)) + word[-1]
        if abbr not in self.dic:
            return True
        if len(self.dic[abbr]) == 1 and word in self.dic[abbr]:
            return True
        return False

        # solution from Pochmann
        #
        # def __init__(self, dictionary):
        #     self.dt = collections.defaultdict(set)
        #     for d in dictionary:
        #         abbr = d[0], len(d), d[-1]
        #         self.dt[abbr].add(d)
        #
        # def isUnique(self, word):
        #     abbr = word[0], len(word), word[-1]
        #     return self.dt[abbr] <= {word}

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)