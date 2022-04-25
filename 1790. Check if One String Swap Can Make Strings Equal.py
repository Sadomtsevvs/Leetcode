from time import time


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        idx_to_change = None
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if i == idx_to_change:
                    continue
                elif idx_to_change is not None:
                    return False
                for j in range(i+1, len(s1)):
                    if s2[j] == s1[i] and s2[i] == s1[j]:
                        idx_to_change = j
                        break
                else:
                    return False
        return True



start_time = time()

_s1 = "bank"
_s2 = "kanb"
_s1 = "attack"
_s2 = "defend"
_s1 = "adcb"
_s2 = "dbca"
_s1 = "caa"
_s2 = "aac"
# Input: s1 = "bank", s2 = "kanb"
# Output: true
# Explanation: For example, swap the first character with the last character of s2 to make "bank".

print(Solution().areAlmostEqual(_s1, _s2))

print("--- %s seconds ---" % (time() - start_time))
