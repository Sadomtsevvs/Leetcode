from time import time


# You are given two strings current and correct representing two 24-hour times.
# 24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59.
# In one operation you can increase the time current by 1, 5, 15, or 60 minutes. You can perform this operation any number of times.
# Return the minimum number of operations needed to convert current to correct.


class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        winners = set()
        losers1 = set()
        losers = set()
        for winner, loser in matches:
            if loser in winners:
                winners -= {loser}
            if loser in losers:
                losers1 -= {loser}
            else:
                losers1 |= {loser}
                losers |= {loser}
            if winner not in losers:
                winners |= {winner}

        return [sorted(list(winners)), sorted(list(losers1))]


start_time = time()

_matches = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
# Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
# Output: [[1,2,10],[4,5,7,8]]
# Explanation:
# Players 1, 2, and 10 have not lost any matches.
# Players 4, 5, 7, and 8 each have lost one match.
# Players 3, 6, and 9 each have lost two matches.
# Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].

print(Solution().findWinners(_matches))

print("--- %s seconds ---" % (time() - start_time))
