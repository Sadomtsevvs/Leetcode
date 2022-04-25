from time import time


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        if k % 2 == 0:
            return (self.kthGrammar(n - 1, k // 2) + 1) % 2
        return self.kthGrammar(n - 1, (k + 1) // 2)

        # brute force (time limit exceed)
        #
        # s = ['0']
        # for i in range(1, n):
        #     s = ['01' if el == '0' else '10' for _ in s for el in _]
        # return s[(k - 1)//2][k % 2 - 1]

# solution from LC comments
#
# def getstr(n, k):
#     if n == 1 or k == 1:
#         return False
#     else:
#         if k % 2 == 0:
#             a = getstr(n - 1, k // 2)
#             return not a
#         elif k % 2 == 1:
#             a = getstr(n - 1, (k + 1) // 2)
#             return a
#
#
# class Solution:
#     def kthGrammar(self, n: int, k: int) -> int:
#         s = getstr(n, k)
#         return int(s)


start_time = time()

_n = 5
_k = 9
_n = 3
_k = 1
# Input: n = 2, k = 2
# Output: 1
# Explanation:
# row 1: 0
# row 2: 01


print(Solution().kthGrammar(_n, _k))

print("--- %s seconds ---" % (time() - start_time))
