from time import time


class Solution:
    def countAndSay(self, n: int) -> str:

        if n <= 1:
            return '1'

        result = ''
        prev = ''
        cnt = 1

        for num in self.countAndSay(n - 1):
            if not prev:
                prev = num
            elif num != prev:
                result += str(cnt) + prev
                cnt = 1
                prev = num
            else:
                cnt += 1
        result += str(cnt) + num

        return result

        # my first solution
        #
        # s = '1'
        # for i in range(1, n):
        #     next_s = ''
        #     cur_cnt = 0
        #     prev_char = ''
        #     for char in s:
        #         if char != prev_char:
        #             if prev_char:
        #                 next_s += str(cur_cnt) + prev_char
        #             cur_cnt = 1
        #             prev_char = char
        #         else:
        #             cur_cnt += 1
        #     next_s += str(cur_cnt) + prev_char
        #     s = next_s
        # return s


start_time = time()

# Example 1:
# Input: n = 1
# Output: "1"
# Explanation: This is the base case.
#
_n = 8
# Example 2:
# Input: n = 4
# Output: "1211"
# Explanation:
# countAndSay(1) = "1"
# countAndSay(2) = say "1" = one 1 = "11"
# countAndSay(3) = say "11" = two 1's = "21"
# countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

print(Solution().countAndSay(_n))

print("--- %s seconds ---" % (time() - start_time))
