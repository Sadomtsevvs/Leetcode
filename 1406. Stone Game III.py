from functools import lru_cache
from time import time
from typing import List


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        @lru_cache
        def dp(player, i):
            if i >= len(stoneValue):
                return {"Alice": 0, "Bob": 0}
            next_player = "Bob" if player == "Alice" else "Alice"
            best_result_next_player = 0
            best_result_player = -float('inf')
            sum_piles = 0
            for x in range(1, min(len(stoneValue) - i + 1, 4)):
                sum_piles += stoneValue[i+x-1]
                results = dp(next_player, i+x)
                cur_result_player = sum_piles + results[player]
                if cur_result_player > best_result_player:
                    best_result_player = cur_result_player
                    best_result_next_player = results[next_player]
            return {player: best_result_player, next_player: best_result_next_player}

        result = dp("Alice", 0);
        if result["Alice"] > result["Bob"]:
            return "Alice"
        elif result["Alice"] < result["Bob"]:
            return "Bob"
        else:
            return "Tie"

        # official solution, great
        #
        # n = len(stoneValue)
        # dp = [0] * (n + 1)
        # for i in range(n - 1, -1, -1):
        #     dp[i] = stoneValue[i] - dp[i + 1]
        #     if i + 2 <= n:
        #         dp[i] = max(dp[i], stoneValue[i] + stoneValue[i + 1] - dp[i + 2])
        #     if i + 3 <= n:
        #         dp[i] = max(dp[i], stoneValue[i] + stoneValue[i + 1]
        #                     + stoneValue[i + 2] - dp[i + 3])
        # if dp[0] > 0:
        #     return "Alice"
        # if dp[0] < 0:
        #     return "Bob"
        # return "Tie"


start_time = time()

# Example 1:
# Input: values = [1,2,3,7]
_values = [1,2,3,7]
# Output: "Bob"
# Explanation: Alice will always lose. Her best move will be to take three piles and the score become 6. Now the score of Bob is 7 and Bob wins.
#
# Example 2:
# Input: values = [1,2,3,-9]
# _values = [1,2,3,-9]
# Output: "Alice"
# Explanation: Alice must choose all the three piles at the first move to win and leave Bob with negative score.
# If Alice chooses one pile her score will be 1 and the next move Bob's score becomes 5. In the next move, Alice will take the pile with value = -9 and lose.
# If Alice chooses two piles her score will be 3 and the next move Bob's score becomes 3. In the next move, Alice will take the pile with value = -9 and also lose.
# Remember that both play optimally so here Alice will choose the scenario that makes her win.
#
# Example 3:
# Input: values = [1,2,3,6]
# _values = [1,2,3,6]
# Output: "Tie"
# Explanation: Alice cannot win this game. She can end the game in a draw if she decided to choose all the first three piles, otherwise she will lose.

# _piles = [1,2,100]

print(Solution().stoneGameIII(_values))

print("--- %s seconds ---" % (time() - start_time))
