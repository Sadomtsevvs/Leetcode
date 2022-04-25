from time import time


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == right:
            return left
        if len(bin(left)) != len(bin(right)):
            return 0
        result = left
        for i in reversed(range(left + 1, right + 1)):
            result &= i
            if result == 0:
                return 0
        return result

        # solution from LC comments
        # don't understand but looks great
        #
        # i = 0
        # while left != right:
        #     left >>= 1
        #     right >>= 1
        #     i += 1
        # return right << i

start_time = time()

# 600000000
# 2147483645
_left = 600000000
_right = 2147483645
# Input: left = 5, right = 7
# Output: 4

print(Solution().rangeBitwiseAnd(_left, _right))

print("--- %s seconds ---" % (time() - start_time))
