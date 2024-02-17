from time import time
from collections import Counter


class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:

        result = []

        counter = Counter(nums)

        def permute(cur, cntr):
            if len(cur) == len(nums):
                result.append(cur)
                return

            for char in cntr:
                if cntr[char] == 0:
                    continue
                cntr[char] -= 1
                permute(cur + [char], cntr)
                cntr[char] += 1

        permute([], counter)
        return result

        # brute-force 2
        #
        # answer = set()
        # pool = set(range(len(nums)))
        #
        # def permutate(rest, cur):
        #     if not rest:
        #         answer.add(tuple(cur))
        #         return
        #     for i in rest:
        #         permutate(rest - {i}, cur + [nums[i]])
        #
        # permutate(pool, [])
        # return [list(el) for el in answer]

        # brute-force 1
        #
        # result = []
        # seen = set()
        #
        # def bt(cur, remain):
        #     if len(cur) == len(nums) and tuple(cur) not in seen:
        #         result.append(cur)
        #         seen.add(tuple(cur))
        #
        #     for i in range(len(remain)):
        #         bt(cur + [remain[i]], remain[:i] + remain[i+1:])
        #
        # bt([], nums)
        #
        # return result


start_time = time()

_nums = [1, 1, 2]
# Output: [[1,1,2], [1,2,1], [2,1,1]]

print(Solution().permuteUnique(_nums))

print("--- %s seconds ---" % (time() - start_time))
