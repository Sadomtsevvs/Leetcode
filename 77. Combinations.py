from time import time


class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:

        result = []

        def backtrack(cur_result, start_number=1):
            if len(cur_result) == k:
                result.append(cur_result)
                return
            for i in range(start_number, n + 1):
                if n - i < k - len(cur_result) - 1:
                    break
                backtrack(cur_result + [i], i + 1)

        backtrack([])
        return result


start_time = time()

_n = 4
_k = 3

print(Solution().combine(_n, _k))

print("--- %s seconds ---" % (time() - start_time))
