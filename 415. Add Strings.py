from time import time


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = ''
        if len(num1) < len(num2):
            num1 = '0'*(len(num2) - len(num1)) + num1
        else:
            num2 = '0'*(len(num1) - len(num2)) + num2
        rem = 0
        for i in range(len(num1)-1, -1, -1):
            sum = int(num1[i]) + int(num2[i]) + rem
            rem = sum // 10
            result = str(sum%10) + result
        if rem == 1:
            result = str(rem) + result
        return result


start_time = time()

_num1 = "456"
_num2 = "0"
# Input: num1 = "456", num2 = "77"
# Output: "533"

print(Solution().addStrings(_num1, _num2))

print("--- %s seconds ---" % (time() - start_time))
