from time import time


class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        time = 0
        for i in range(len(tickets)):
            if tickets[i] >= tickets[k]:
                if i > k:
                    time += tickets[k] - 1
                else:
                    time += tickets[k]
            else:
                time += tickets[i]
        return time


start_time = time()

_tickets = [5, 1, 1, 1]
_k = 0

print(Solution().timeRequiredToBuy(_tickets, _k))

print("--- %s seconds ---" % (time() - start_time))