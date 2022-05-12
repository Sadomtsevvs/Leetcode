from time import time


class Solution:
    def countPrimes(self, n: int) -> int:

        # primes = []
        # for i in range(2, n):
        #     sqrt_n = n ** 0.5
        #     for prime in primes:
        #         if i % prime == 0:
        #             break
        #         if prime > sqrt_n:
        #             primes.append(i)
        #             break
        #     else:
        #         primes.append(i)
        # return len(primes)

        # Eratosthenes
        if n < 3:
            return 0
        primes = [1] * n
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i**2, n, i):
                    primes[j] = 0
        return sum(primes) - 2


start_time = time()

_n = 1
# _n = 10
# _n = 499979
# _n = 5000000
# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# Input: n = 499979
# Output: 41537
# Input: n = 5000000
# Output: 348513

print(Solution().countPrimes(_n))

print("--- %s seconds ---" % (time() - start_time))
