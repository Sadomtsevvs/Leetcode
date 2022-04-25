from time import time


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = [[] for _ in range(numRows)]
        ind = 0
        while ind < len(s):
            for j in range(min(numRows, len(s) - ind)):
                res[j].append(s[ind])
                ind += 1
            if ind == len(s):
                break
            for j in range(numRows - 2, numRows - 2 - (len(s) - ind) if len(s) - ind < numRows - 2 else 0, -1):
                res[j].append(s[ind])
                ind += 1
        result = ''
        for i in range(numRows):
            result += ''.join(res[i])
        return result


start_time = time()

_s = "PAYPALISHIRING"
_numRows = 3

print(Solution().convert(_s, _numRows))

print("--- %s seconds ---" % (time() - start_time))
