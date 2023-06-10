from functools import cache
from time import time
from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        @cache
        def dp(player, i, m):
            if i >= len(piles):
                return {"Alice": 0, "Bob": 0}
            next_player = "Bob" if player == "Alice" else "Alice"
            best_result_next_player = 0
            best_result_player = 0
            sum_piles = 0
            for x in range(1, min(len(piles) - i + 1, 2 * m + 1)):
                sum_piles += piles[i+x-1]
                results = dp(next_player, i+x, max(m, x))
                cur_result_player = sum_piles + results[player]
                if cur_result_player > best_result_player:
                    best_result_player = cur_result_player
                    best_result_next_player = results[next_player]
            return {player: best_result_player, next_player: best_result_next_player}

        return dp("Alice", 0, 1)["Alice"]

        # official solution
        #
        # n = len(piles)
        #
        # def f(p, i, m):
        #     if i == n:
        #         return 0
        #     res = 1000000 if p == 1 else -1
        #     s = 0
        #     for x in range(1, min(2 * m, n - i) + 1):
        #         s += piles[i + x - 1]
        #         if p == 0:
        #             res = max(res, s + f(1, i + x, max(m, x)))
        #         else:
        #             res = min(res, f(0, i + x, max(m, x)))
        #     return res
        #
        # return f(0, 0, 1)

start_time = time()

# Example 1:
# Input: piles = [2,7,9,4,4]
_piles = [2,7,9,4,4]
# Output: 10
# Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger.
#
# Example 2:
# Input: piles = [1,2,3,4,5,100]
_piles = [1,2,3,4,5,100]
# Output: 104

# _piles = [1,2,100]

print(Solution().stoneGameII(_piles))

print("--- %s seconds ---" % (time() - start_time))
