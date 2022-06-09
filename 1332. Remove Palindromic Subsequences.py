from time import time


class Solution:
    def removePalindromeSub(self, s: str) -> int:

        def longest_palindrom(string):
            beg, end = 0, 0
            max_len = 1
            for i in range(1, len(string)):
                cur_len = 1
                for j in range(min(i, len(string) - i - 1)):
                    if string[i-j-1] != string[i+j+1]:
                        break
                    cur_len += 2
                if cur_len > max_len:
                    max_len = cur_len
                    beg, end = i-j-1, i+j+1
                cur_len = 0
                for j in range(min(i, len(string) - i)):
                    if string[i-j-1] != string[i+j]:
                        break
                    cur_len += 2
                if cur_len > max_len:
                    max_len = cur_len
                    beg, end = i-j-1, i+j
            return beg, end

        ans = 0
        while s:
            beg, end = longest_palindrom(s)
            s = s[:beg] + s[end+1:]
            ans += 1
        return min(ans, 2)

        # Lee solution
        #
        # return 2 - (s == s[::-1]) - (s == "")

        # Babichev
        #
        # return 0 if s == "" else 1 if s == s[::-1] else 2


start_time = time()

_s = "baabb"
_s = "abbaaaab"
# _s = "abb"
# Input: s = "baabb"
# Output: 2
# Explanation: "baabb" -> "b" -> "".
# Remove palindromic subsequence "baab" then "b".

print(Solution().removePalindromeSub(_s))

print("--- %s seconds ---" % (time() - start_time))