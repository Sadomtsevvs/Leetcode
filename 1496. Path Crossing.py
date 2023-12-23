from time import time
from typing import List


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        passed = {(0, 0)}
        cur = [0, 0]
        for d in path:
            match d:
                case 'N':
                    cur[1] += 1
                case 'S':
                    cur[1] -= 1
                case 'E':
                    cur[0] += 1
                case 'W':
                    cur[0] -= 1
                case _:
                    raise ValueError("Not a point")
            point = tuple(cur)
            if point in passed:
                return True
            passed.add(point)
        return False


start_time = time()

# Example 1:
# Input: path = "NES"
# Output: false
# Explanation: Notice that the path doesn't cross any point more than once.
#
# Example 2:
# Input: path = "NESWW"
_path = "NESWW"
# Output: true
# Explanation: Notice that the path visits the origin twice.

print(Solution().isPathCrossing(_path))

print("--- %s seconds ---" % (time() - start_time))
