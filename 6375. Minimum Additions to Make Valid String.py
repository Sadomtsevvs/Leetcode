from time import time


class Solution:
    def addMinimum(self, word: str) -> int:
        ans = 0
        prev = ''
        for char in word:
            if prev == '':
                if char == 'a':
                    prev = 'a'
                elif char == 'b':
                    prev = 'b'
                    ans += 1
                else:
                    ans += 2
            elif prev == 'a':
                if char == 'a':
                    ans += 2
                elif char == 'b':
                    prev = 'b'
                else:
                    prev = ''
                    ans += 1
            elif prev == 'b':
                if char == 'a':
                    prev = 'a'
                    ans += 1
                elif char == 'b':
                    ans += 2
                    prev = 'b'
                else:
                    prev = ''
        if prev == 'a':
            ans += 2
        elif prev == 'b':
            ans += 1
        return ans




start_time = time()

# Example 1:
# Input: word = "b"
_word = "b"
# Output: 2
# Explanation: Insert the letter "a" right before "b", and the letter "c" right next to "a" to obtain the valid string "abc".
#
# Example 2:
# Input: word = "aaa"
_word = "aaa"
# Output: 6
# Explanation: Insert letters "b" and "c" next to each "a" to obtain the valid string "abcabcabc".
#
# Example 3:
# Input: word = "abc"
_word = "abc"
# Output: 0
# Explanation: word is already valid. No modifications are needed.
_word = "bbc"

print(Solution().addMinimum(_word))

print("--- %s seconds ---" % (time() - start_time))
