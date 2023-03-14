from time import time
from typing import List


class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        guesses =


start_time = time()

_edges = [[0,1],[1,2],[1,3],[4,2]]
_guesses = [[1,3],[0,1],[1,0],[2,4]]
_k = 3

# Example 1:
# Input: edges = [[0,1],[1,2],[1,3],[4,2]], guesses = [[1,3],[0,1],[1,0],[2,4]], k = 3
# Output: 3
# Explanation:
# Root = 0, correct guesses = [1,3], [0,1], [2,4]
# Root = 1, correct guesses = [1,3], [1,0], [2,4]
# Root = 2, correct guesses = [1,3], [1,0], [2,4]
# Root = 3, correct guesses = [1,0], [2,4]
# Root = 4, correct guesses = [1,3], [1,0]
# Considering 0, 1, or 2 as root node leads to 3 correct guesses.
#
# Example 2:
# Input: edges = [[0,1],[1,2],[2,3],[3,4]], guesses = [[1,0],[3,4],[2,1],[3,2]], k = 1
# Output: 5
# Explanation:
# Root = 0, correct guesses = [3,4]
# Root = 1, correct guesses = [1,0], [3,4]
# Root = 2, correct guesses = [1,0], [2,1], [3,4]
# Root = 3, correct guesses = [1,0], [2,1], [3,2], [3,4]
# Root = 4, correct guesses = [1,0], [2,1], [3,2]
# Considering any node as root will give at least 1 correct guess.

print(Solution().rootCount(_edges, _guesses, _k))

print("--- %s seconds ---" % (time() - start_time))
