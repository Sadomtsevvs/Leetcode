from time import time


class Solution:
    def partitionString(self, s: str) -> int:
        ans = 1
        bucket = set()
        for char in s:
            if char in bucket:
                ans += 1
                bucket = {char}
            else:
                bucket.add(char)
        return ans


start_time = time()

# Example 1:
# Input: s = "abacaba"
# Output: 4
# Explanation:
# Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
# It can be shown that 4 is the minimum number of substrings needed.
#
# Example 2:
# Input: s = "ssssss"
# Output: 6
# Explanation:
# The only valid partition is ("s","s","s","s","s","s").

_s = "hdklqkcssgxlvehva" # hdklq + kcs + sgxlveh + va
# Output: 2
# Expected: 4

print(Solution().partitionString(_s))

print("--- %s seconds ---" % (time() - start_time))
