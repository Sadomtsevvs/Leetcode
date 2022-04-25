from time import time


class Solution:
    def myAtoi(self, s: str) -> int:
        minresult = -2 ** 31
        maxresult = 2 ** 31 - 1
        result = ''
        getnumber = False
        getsign = False
        for i in s:
            if i.isdigit():
                result += i
                getnumber = True
                getsign = True
                continue
            if not getnumber:
                if not getsign:
                    if i == ' ':
                        continue
                    if i == '+' or i == '-':
                        result += i
                        getsign = True
                        continue
                return 0
            break
        if not getnumber:
            return 0
        result = int(result)
        if result < minresult:
            return minresult
        if result > maxresult:
            return maxresult
        return result


start_time = time()

_s = " + 413"

print(Solution().myAtoi(_s))

print("--- %s seconds ---" % (time() - start_time))