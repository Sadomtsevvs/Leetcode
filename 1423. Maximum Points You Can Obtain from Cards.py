from functools import lru_cache
from time import time
from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        if k == len(cardPoints):
            return sum(cardPoints)

        n = len(cardPoints)

        acc_l, acc_r = [0] * n, [0] * n
        s = 0
        for i in range(k):
            acc_l[i] = cardPoints[i] + s
            s = acc_l[i]
        s = 0
        for i in range(k):
            acc_r[i] = cardPoints[n - 1 - i] + s
            s = acc_r[i]

        ans = max(acc_l[k - 1], acc_r[k - 1])
        for i in range(0, k - 1):
            ans = max(ans, acc_l[i] + acc_r[k - i - 2])
        return ans


        # TLE
        #
        # @lru_cache
        # def dp(first, last, remain):
        #     if first > last or remain == 0:
        #         return 0
        #     return max(cardPoints[first] + dp(first+1, last, remain-1),
        #                cardPoints[last] + dp(first, last-1, remain-1))
        #
        # return dp(0, len(cardPoints)-1, k)

        # O(1) memory solution from LC comments
        #
        # int n = cardPoints.length, lSum = 0;
        # for(int i = 0; i < k; ++i){
        #     lSum += cardPoints[i];
        # }
        # int max = lSum;
        # for(int rSum = 0, i = 0; i < k; ++i){
        #     rSum += cardPoints[n-1-i];
        #     lSum -= cardPoints[k-1-i];
        #     max = Math.max(max,lSum+rSum);
        # }
        # return max;

        # LC 2
        #
        # ans = win = 0
        # for i in range(-k, k):
        #     win += cardPoints[i]
        #     if i >= 0:
        #         win -= cardPoints[i - k]
        #     ans = max(win, ans)
        # return ans



start_time = time()

_cardPoints = [1,2,3,4,5,6,1]
_k = 3
# Input: cardPoints = [1,2,3,4,5,6,1], k = 3
# Output: 12
# Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize
# your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
print(Solution().maxScore(_cardPoints, _k))

print("--- %s seconds ---" % (time() - start_time))
