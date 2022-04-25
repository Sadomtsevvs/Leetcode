from time import time


class Solution:
    def calPoints(self, ops: list[str]) -> int:
        result = []
        for o in ops:
            if o == "D":
                result.append(result[-1] * 2)
            elif o == "C":
                result.pop()
            elif o == '+':
                result.append(result[-1] + result[-2])
            else:
                result.append(int(o))
        return sum(result)


start_time = time()

_ops = ["5","2","C","D","+"]
_ops = ["5","-2","4","C","D","9","+","+"]
# Input: ops = ["5","2","C","D","+"]
# Output: 30
# Explanation:
# "5" - Add 5 to the record, record is now [5].
# "2" - Add 2 to the record, record is now [5, 2].
# "C" - Invalidate and remove the previous score, record is now [5].
# "D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
# "+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
# The total sum is 5 + 10 + 15 = 30.

print(Solution().calPoints(_ops))

print("--- %s seconds ---" % (time() - start_time))
