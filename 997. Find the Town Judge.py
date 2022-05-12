from time import time


class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        judges = set(range(1, n+1))
        for (who, whom) in trust:
            judges -= {who}
        if len(judges) != 1:
            return -1
        # control
        judge = judges.pop()
        not_judges = set()
        for (who, whom) in trust:
            if whom == judge:
                not_judges |= {who}
        return judge if len(not_judges) == n-1 else -1

        # solution from Lee,
        #
        # count = [0] * (N + 1)
        # for i, j in trust:
        #     count[i] -= 1
        #     count[j] += 1
        # for i in range(1, N + 1):
        #     if count[i] == N - 1:
        #         return i
        # return -1


start_time = time()

_n = 3
_trust = [[1,3],[2,3]]
# Input: n = 3, trust = [[1,3],[2,3]]
# Output: 3

print(Solution().findJudge(_n, _trust))

print("--- %s seconds ---" % (time() - start_time))
