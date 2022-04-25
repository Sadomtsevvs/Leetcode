from time import time


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:

        result = [[]]

        def backtrack(remain_set, cur_result):

            if not remain_set:
                return

            passed = set()

            for el in remain_set:
                result.append(cur_result + [el])
                backtrack(remain_set - {el} - passed, cur_result + [el])
                passed.add(el)

        backtrack(set(nums), [])

        return result

        # another interesting solution from LC
        #
        # answer = [[]]
        #
        # for num in nums:
        #     answer += [item + [num] for item in answer]
        #
        # return answer

start_time = time()

_nums = [1, 2, 3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

print(Solution().subsets(_nums))

print("--- %s seconds ---" % (time() - start_time))
