from time import time
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n + 1):
            val = ''
            if i % 3 == 0:
                val += 'Fizz'
            if i % 5 == 0:
                val += 'Buzz'
            result.append(str(i) if not val else val)
        return result


start_time = time()

_n = 15
# Input: n = 15
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

print(Solution().fizzBuzz(_n))

print("--- %s seconds ---" % (time() - start_time))
