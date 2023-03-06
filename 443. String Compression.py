from time import time
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        pointer = 0
        prev = None
        counter = 0
        for i in range(len(chars)):
            char = chars[i]
            if char != prev:
                if counter > 1:
                    for n in str(counter):
                        chars[pointer] = n
                        pointer += 1
                chars[pointer] = char
                pointer += 1
                counter = 0
                prev = char
            counter += 1

        if counter > 1:
            for n in str(counter):
                chars[pointer] = n
                pointer += 1

        return pointer


start_time = time()

_chars = ["a", "a", "b", "b", "c", "c", "c"]

# Example 1:
# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
#
# Example 2:
# Input: chars = ["a"]
# Output: Return 1, and the first character of the input array should be: ["a"]
# Explanation: The only group is "a", which remains uncompressed since it's a single character.
#
_chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# Example 3:
# Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
# Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

_chars = ["a","a","a","b","b","a","a"]

print(Solution().compress(_chars))

print("--- %s seconds ---" % (time() - start_time))
