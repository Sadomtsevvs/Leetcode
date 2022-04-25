from time import time


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:

        result = []

        def backtrack(cur_result, remain_set):
            if len(cur_result) == len(nums):
                result.append(cur_result)
                return
            for el in remain_set:
                backtrack(cur_result + [el], remain_set - {el})

        backtrack([], set(nums))

        return result


start_time = time()

_nums = [1, 2, 3]

print(Solution().permute(_nums))

print("--- %s seconds ---" % (time() - start_time))
