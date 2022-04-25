from time import time


class Solution:
    def maxScoreIndices(self, nums: list[int]) -> list[int]:
        result = []
        score_left, score_right = 0, nums.count(1)
        max_score = score_left + score_right
        max_score0 = max_score
        for num in nums:
            if num == 0:
                score_left += 1
            else:
                score_right -= 1
            max_score = max(max_score, score_left + score_right)
        if max_score0 == max_score:
            result.append(0)
        score_left, score_right = 0, nums.count(1)
        for i in range(len(nums)):
            if nums[i] == 0:
                score_left += 1
            else:
                score_right -= 1
            if score_left + score_right == max_score:
                result.append(i+1)
        return result



start_time = time()

_nums = [1,1]
# Input: nums = [0,0,1,0]
# Output: [2,4]
# Explanation: Division at index
# - 0: numsleft is []. numsright is [0,0,1,0]. The score is 0 + 1 = 1.
# - 1: numsleft is [0]. numsright is [0,1,0]. The score is 1 + 1 = 2.
# - 2: numsleft is [0,0]. numsright is [1,0]. The score is 2 + 1 = 3.
# - 3: numsleft is [0,0,1]. numsright is [0]. The score is 2 + 0 = 2.
# - 4: numsleft is [0,0,1,0]. numsright is []. The score is 3 + 0 = 3.
# Indices 2 and 4 both have the highest possible division score 3.
# Note the answer [4,2] would also be accepted.

print(Solution().maxScoreIndices(_nums))

print("--- %s seconds ---" % (time() - start_time))