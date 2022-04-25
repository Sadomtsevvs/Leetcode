from time import time


class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:

        result = []
        seen = set()

        def bt(cur, remain):
            if len(cur) == len(nums) and tuple(cur) not in seen:
                result.append(cur)
                seen.add(tuple(cur))

            for i in range(len(remain)):
                bt(cur + [remain[i]], remain[:i] + remain [i+1:])

        bt([], nums)

        return result


start_time = time()

_nums = [1, 1, 2]
# Output: [[1,1,2], [1,2,1], [2,1,1]]

print(Solution().permuteUnique(_nums))

print("--- %s seconds ---" % (time() - start_time))
