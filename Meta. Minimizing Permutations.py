# from functools import reduce
import collections
from time import time


class Solution:
    def minOperations(self, arr):
        ans = 0
        while True:
            first = None
            for i in range(1, len(arr)):
                if arr[i] < arr[i-1]:
                    if first is None:
                        first = i - 1
                    last = i
                elif first is not None:
                    break
            if first is None:
                break
            for i in range(first, (first + last + 1) // 2):
                arr[first + i], arr[last - i] = arr[last - i], arr[first + i]
            ans += 1
        return ans

        # graph with bfs solution
        #
        # target = "".join([str(num) for num in sorted(arr)])
        # curr = "".join([str(num) for num in arr])
        # queue = collections.deque([(0, curr)])  # In the queue we store (<level>, <permutation>)
        # visited = set([curr])
        #
        # while queue:
        #     level, curr = queue.popleft()
        #
        #     if curr == target:
        #         return level  # We are done
        #
        #     for i in range(len(curr)-1):
        #         for j in range(i+1, len(curr)):
        #             # Reverse elements between i and j (inclusive)
        #             # Note we are operating on strings here, so we create a new copy
        #             permutation = curr[:i] + curr[i:j + 1][::-1] + curr[j + 1:]
        #
        #             if permutation not in visited:
        #                 visited.add(permutation)
        #                 queue.append((level + 1, permutation))
        #
        # return -1


start_time = time()

_arr = [3, 1, 2]
_arr = [1, 2, 5, 4, 3]
# Example
# If N = 3, and P = (3, 1, 2), we can do the following operations:
# Select (1, 2) and reverse it: P = (3, 2, 1).
# Select (3, 2, 1) and reverse it: P = (1, 2, 3).
# output = 2

print(Solution().minOperations(_arr))

print("--- %s seconds ---" % (time() - start_time))
