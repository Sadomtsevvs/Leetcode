from time import time


class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:

        result = []

        def bt(cur, remain, start_index):
            if remain == 0:
                result.append(cur)
                return
            elif remain < 0:
                return
            for i in range(start_index, len(candidates)):
                # skip if meet the same number
                if i > start_index and candidates[i] == candidates[i - 1]:
                    continue
                bt(cur + [candidates[i]], remain - candidates[i], i + 1)

        candidates.sort()

        bt([], target, 0)

        return result


start_time = time()

# _candidates = [10,1,2,7,6,1,5]
_candidates = [3, 1, 3, 5, 1, 1]
# _candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
# _target = 8
_target = 8
# _target = 27
# Output: [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]

print(Solution().combinationSum2(_candidates, _target))

print("--- %s seconds ---" % (time() - start_time))
