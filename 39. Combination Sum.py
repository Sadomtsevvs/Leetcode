from time import time


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        result = []

        def bt(cur, remain, start_index):
            if remain == 0:
                result.append(cur)
                return
            elif remain < 0:
                return
            for i in range(start_index, len(candidates)):
                bt(cur + [candidates[i]], remain - candidates[i], i)

        bt([], target, 0)

        return result


start_time = time()

_candidates = [2,7,6,3,5,1]
_target = 9
# Output: [[2,2,3],[7]]

print(Solution().combinationSum(_candidates, _target))

print("--- %s seconds ---" % (time() - start_time))
