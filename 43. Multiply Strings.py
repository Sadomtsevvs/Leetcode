from time import time


class Solution:

    def multiply(self, num1: str, num2: str) -> str:
        results = []
        for j in range(len(num2)-1, -1, -1):
            carry = 0
            result = 0
            for i in range(len(num1) - 1, -1, -1):
                prod = int(num1[i]) * int(num2[j]) + carry
                carry = prod // 10
                result += prod%10 * 10**(len(num1)-i-1)
            result += carry*(10**len(num1))
            result *= 10**(len(num2)-j-1)
            results.append(result)
        return str(sum(results))


start_time = time()

_num1 = "123"
_num2 = "456"
_num1 = "123"
_num2 = "0"

# Input: num1 = "123", num2 = "456"
# Output: "56088"

print(Solution().multiply(_num1, _num2))

print("--- %s seconds ---" % (time() - start_time))