from time import time


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        d = 'ZABCDEFGHIJKLMNOPQRSTUVWXY'
        ans = ''
        while columnNumber > 0:
            columnNumber, m = divmod(columnNumber, 26)
            ans = d[m] + ans
            if m == 0:
                columnNumber -= 1
        return ans


start_time = time()

# Example 1:
# Input: columnNumber = 1
# Output: "A"
#
# Example 2:
# Input: columnNumber = 28
# Output: "AB"
#
# Example 3:
# Input: columnNumber = 701
_columnNumber = 701
# Output: "ZY"

print(Solution().convertToTitle(_columnNumber))

print("--- %s seconds ---" % (time() - start_time))
