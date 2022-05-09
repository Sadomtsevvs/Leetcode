from time import time


class Solution:
    def findEncryptedWord(self, s):
        if len(s) <= 1:
            return s
        a, b = divmod(len(s), 2)
        if b == 1:
            mid = a
        else:
            mid = a - 1
        return s[mid] + self.findEncryptedWord(s[:mid]) + self.findEncryptedWord(s[mid+1:])


start_time = time()

_s = "facebook"
# S = "facebook"
# R = "eafcobok"

print(Solution().findEncryptedWord(_s))

print("--- %s seconds ---" % (time() - start_time))
