from time import time


class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        to_visit = set(range(1, len(rooms)))
        keys = set(rooms[0])
        while keys:
            key = keys.pop()
            if key in to_visit:
                to_visit -= {key}
                for next_key in rooms[key]:
                    if next_key in to_visit:
                        keys.add(next_key)
        return len(to_visit) == 0


start_time = time()

_rooms = [[1],[2],[3],[]]
# Input: rooms = [[1],[2],[3],[]]
# Output: true
# Explanation:
# We visit room 0 and pick up key 1.
# We then visit room 1 and pick up key 2.
# We then visit room 2 and pick up key 3.
# We then visit room 3.
# Since we were able to visit every room, we return true.

print(Solution().canVisitAllRooms(_rooms))

print("--- %s seconds ---" % (time() - start_time))
