from time import time
from typing import List


class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        nums.sort()
        divisors = list(set(divisors))
        divisors.sort()
        answers = dict()
        point_nums = 0
        for div in divisors:
            while point_nums < len(nums) and nums[point_nums] < div:
                point_nums += 1
            divs = 0
            for i in range(point_nums, len(nums)):
                if nums[i] % div == 0:
                    divs += 1
            answers[div] = divs
        divs = 0
        answer = min(answers.keys())
        for key, value in answers.items():
            if value > divs:
                answer = key
                divs = value
            elif value == divs:
                answer = min(answer, key)
        return answer


start_time = time()

# Example 1:
# Input: nums = [4,7,9,3,9], divisors = [5,2,3]
_nums = [4,7,9,3,9]
_divisors = [5,2,3]
# Output: 3
# Explanation: The divisibility score for every element in divisors is:
# The divisibility score of divisors[0] is 0 since no number in nums is divisible by 5.
# The divisibility score of divisors[1] is 1 since nums[0] is divisible by 2.
# The divisibility score of divisors[2] is 3 since nums[2], nums[3], and nums[4] are divisible by 3.
# Since divisors[2] has the maximum divisibility score, we return it.
#
# Example 2:
# Input: nums = [20,14,21,10], divisors = [5,7,5]
# _nums = [20,14,21,10]
# _divisors = [5,7,5]
# Output: 5
# Explanation: The divisibility score for every element in divisors is:
# The divisibility score of divisors[0] is 2 since nums[0] and nums[3] are divisible by 5.
# The divisibility score of divisors[1] is 2 since nums[1] and nums[2] are divisible by 7.
# The divisibility score of divisors[2] is 2 since nums[0] and nums[3] are divisible by 5.
# Since divisors[0], divisors[1], and divisors[2] all have the maximum divisibility score, we return the minimum of them (i.e., divisors[2]).
#
# Example 3:
# Input: nums = [12], divisors = [10,16]
# _nums = [12]
# _divisors = [10,16]
# Output: 10
# Explanation: The divisibility score for every element in divisors is:
# The divisibility score of divisors[0] is 0 since no number in nums is divisible by 10.
# The divisibility score of divisors[1] is 0 since no number in nums is divisible by 16.
# Since divisors[0] and divisors[1] both have the maximum divisibility score, we return the minimum of them (i.e., divisors[0]).

print(Solution().maxDivScore(_nums, _divisors))

print("--- %s seconds ---" % (time() - start_time))
