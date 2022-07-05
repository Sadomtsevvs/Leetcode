from time import time
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:

        #O(n)
        #
        ans = len(ratings)
        candies_left_right = [1] * len(ratings)
        candies_right_left = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1] and candies_left_right[i] <= candies_left_right[i-1]:
                add = candies_left_right[i-1] - candies_left_right[i] + 1
                candies_left_right[i] += add
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i+1] and candies_right_left[i] <= candies_right_left[i+1]:
                add = candies_right_left[i+1] - candies_right_left[i] + 1
                candies_right_left[i] += add
        for i in range(len(ratings)):
            ans += max(candies_left_right[i], candies_right_left[i]) - 1
        return ans

        # brute - force, O(n**2)
        #
        # ans = len(ratings)
        # candies = [1] * len(ratings)
        # add_candies = True
        # while add_candies:
        #     add_candies = False
        #     for i in range(1, len(ratings)):
        #         if ratings[i] > ratings[i-1] and candies[i] <= candies[i-1]:
        #             add = candies[i-1] - candies[i] + 1
        #             ans += add
        #             candies[i] += add
        #             add_candies = True
        #     for i in range(len(ratings) - 2, -1, -1):
        #         if ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
        #             add = candies[i+1] - candies[i] + 1
        #             ans += add
        #             candies[i] += add
        #             add_candies = True
        # return ans


start_time = time()

_ratings = [1,0,2]
# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

# _ratings = [1,2,2]
# Input: ratings = [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
# The third child gets 1 candy because it satisfies the above two conditions.

print(Solution().candy(_ratings))

print("--- %s seconds ---" % (time() - start_time))
