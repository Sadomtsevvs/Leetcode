from time import time


class Solution:
    def numberOfSteps(self, num: int) -> int:
        if not num:
            return 0
        ans = 0
        while num > 0:
            num, b = divmod(num, 2)
            if b == 0:
                ans += 1
            else:
                ans += 2
        return ans - 1

        # from LC
        #
        # steps = num == 0
        # while num > 0:
        #     steps += 1 + (num & 1)
        #     num >>= 1
        # return steps - 1


start_time = time()

_num = 14
# Input: num = 14
# Output: 6
# Explanation:
# Step 1) 14 is even; divide by 2 and obtain 7.
# Step 2) 7 is odd; subtract 1 and obtain 6.
# Step 3) 6 is even; divide by 2 and obtain 3.
# Step 4) 3 is odd; subtract 1 and obtain 2.
# Step 5) 2 is even; divide by 2 and obtain 1.
# Step 6) 1 is odd; subtract 1 and obtain 0.

print(Solution().numberOfSteps(_num))

print("--- %s seconds ---" % (time() - start_time))
