from time import time
from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        ans = 0
        for i in range(len(bombs)):
            cur_ans = 1
            seen = {i}
            next_bombs = [bombs[i]]
            while next_bombs:
                x0, y0, r0 = next_bombs.pop()
                for j in range(len(bombs)):
                    if j in seen:
                        continue
                    x1, y1, r1 = bombs[j]
                    if (x1 - x0)**2 + (y1 - y0)**2 <= r0**2 and j not in seen:
                        cur_ans += 1
                        next_bombs.append(bombs[j])
                        seen.add(j)
            ans = max(cur_ans, ans)
        return ans

    # official dfs solution
    #
    # graph = collections.defaultdict(list)
    # n = len(bombs)
    #
    # # Build the graph
    # for i in range(n):
    #     for j in range(n):
    #         xi, yi, ri = bombs[i]
    #         xj, yj, _ = bombs[j]
    #
    #         # Create a path from i to j, if bomb i detonates bomb j.
    #         if ri ** 2 >= (xi - xj) ** 2 + (yi - yj) ** 2:
    #             graph[i].append(j)
    #
    # def dfs(i):
    #     stack = [i]
    #     visited = set([i])
    #     while stack:
    #         cur = stack.pop()
    #         for neib in graph[cur]:
    #             if neib not in visited:
    #                 visited.add(neib)
    #                 stack.append(neib)
    #     return len(visited)
    #
    # answer = 0
    # for i in range(n):
    #     answer = max(answer, dfs(i))
    #
    # return answer


start_time = time()

# Example 1:
# Input: bombs = [[2,1,3],[6,1,4]]
# Output: 2
# Explanation:
# The above figure shows the positions and ranges of the 2 bombs.
# If we detonate the left bomb, the right bomb will not be affected.
# But if we detonate the right bomb, both bombs will be detonated.
# So the maximum bombs that can be detonated is max(1, 2) = 2.
#
# Example 2:
# Input: bombs = [[1,1,5],[10,10,5]]
# Output: 1
# Explanation:
# Detonating either bomb will not detonate the other bomb, so the maximum number of bombs that can be detonated is 1.
#
# Example 3:
# Input: bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
# Output: 5
# Explanation:
# The best bomb to detonate is bomb 0 because:
# - Bomb 0 detonates bombs 1 and 2. The red circle denotes the range of bomb 0.
# - Bomb 2 detonates bomb 3. The blue circle denotes the range of bomb 2.
# - Bomb 3 detonates bomb 4. The green circle denotes the range of bomb 3.
# Thus all 5 bombs are detonated.

print(Solution().maxStrength(_nums))

print("--- %s seconds ---" % (time() - start_time))
