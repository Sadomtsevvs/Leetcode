from time import time


class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:

        """  solution from comments
        nums.sort()
        seen = set()
        result = []

        def bt(cur, remain):
            if tuple(cur) not in seen:
                result.append(cur)
                seen.add(tuple(cur))

            for i in range(len(remain)):
                bt(cur + [remain[i]], remain[i + 1:])

        bt([], nums)
        return result
        """

        nums.sort()
        result = [[]]
        seen = set()

        for num in nums:
            add_to_answer = [item + [num] for item in result if tuple(item + [num]) not in seen]
            result += add_to_answer
            for added in add_to_answer:
                seen.add(tuple(added))

        return result


start_time = time()

_nums = [4,4,4,1,4]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

print(Solution().subsetsWithDup(_nums))

print("--- %s seconds ---" % (time() - start_time))
