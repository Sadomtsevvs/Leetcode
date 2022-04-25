from time import time


class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        # official solution, i can't solve
        people.sort()
        i, j = 0, len(people) - 1
        ans = 0
        while i <= j:
            ans += 1
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
        return ans




start_time = time()

_people = [3,2,2,1]
_limit = 3
# Input: people = [3,2,2,1], limit = 3
# Output: 3
# Explanation: 3 boats (1, 2), (2) and (3)

print(Solution().numRescueBoats(_people, _limit))

print("--- %s seconds ---" % (time() - start_time))
