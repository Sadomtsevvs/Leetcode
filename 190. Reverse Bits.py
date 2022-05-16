from time import time


class Solution:
    def reverseBits(self, n: int) -> int:
        return int('0b' + bin(n)[2:][::-1] + '0' * (34 - len(bin(n))), 2)

        # another solution, without string
        #
        # ans = 0
        # for _ in range(32):
        #     ans <<= 1
        #     if n % 2 == 1:
        #         ans += 1
        #     n >>= 1
        # return ans


start_time = time()

_n = 0b00000010100101000001111010011100

print(Solution().reverseBits(_n))

print("--- %s seconds ---" % (time() - start_time))
