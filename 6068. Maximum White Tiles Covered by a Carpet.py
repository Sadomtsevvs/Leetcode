from time import time
from typing import List


class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        left, right = 0, 0
        result = 0
        covered = 0
        while left < len(tiles):
            # if pointers meet let's start cover tiles again
            if left == right:
                covered = tiles[left][1] - tiles[left][0] + 1
                right += 1
            last_covered = 0
            # move right pointer until it intersects with the left one
            while right < len(tiles) and tiles[right][0] - tiles[left][0] + 1 <= carpetLen:
                last_covered = min(tiles[right][1], tiles[left][0] + carpetLen - 1) - tiles[right][0] + 1
                covered += last_covered
                right += 1
            result = max(result, covered)
            if right == len(tiles):
                break
            # move left pointer and reduce the covered tiles
            covered -= (tiles[left][1] - tiles[left][0] + 1)
            left += 1
            # return right pointer one step back and also reduce covered tiles
            if last_covered > 0:
                covered -= last_covered
                right -= 1
        return min(result, carpetLen)


start_time = time()

# _tiles = [[1, 5], [10, 11], [12, 18], [20, 25], [30, 32]]
# _carpetLen = 10
_tiles = [[10,12],[1,1]]
_carpetLen = 2
# _tiles = [[7917,7925], [7930,7950], [7969,7987], [7994,7995], [8003,8011], [8013,8020], [8027,8035], [8051,8057],[8074,8089], [8096,8104], [8123,8139]]
# _carpetLen = 9854
# Input: tiles = [[1,5],[10,11],[12,18],[20,25],[30,32]], carpetLen = 10
# Output: 9
# Explanation: Place the carpet starting on tile 10.
# It covers 9 white tiles, so we return 9.
# Note that there may be other places where the carpet covers 9 white tiles.
# It can be shown that the carpet cannot cover more than 9 white tiles.

print(Solution().maximumWhiteTiles(_tiles, _carpetLen))

print("--- %s seconds ---" % (time() - start_time))
