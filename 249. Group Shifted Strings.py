from collections import defaultdict
from time import time
from typing import List


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for word in strings:
            key = []
            base_shift = ord(word[0])
            for i in range(1, len(word)):
                char_shift = (ord(word[i]) - base_shift) % 26
                # char_shift = ord(word[i]) - base_shift
                # if char_shift < 0:
                #     char_shift += 26
                key.append(str(char_shift))
            dic['.'.join(key)].append(word)
        return dic.values()


start_time = time()

_strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
# Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
# Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
_strings = ["abc","am"]

print(Solution().groupStrings(_strings))

print("--- %s seconds ---" % (time() - start_time))
