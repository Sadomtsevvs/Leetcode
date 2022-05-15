from time import time
from typing import List


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:

        # TLE

        # ans = [1]
        #
        # def recur(cur_len, cur_ind, cur_res):
        #
        #     if cur_res == 0:
        #         return
        #     if cur_len > ans[0]:
        #         ans[0] = cur_len
        #
        #     for j in range(cur_ind, len(candidates)):
        #         recur(cur_len + 1, j + 1, cur_res & candidates[j])
        #
        # for i in range(len(candidates)):
        #     recur(1, i + 1, candidates[i])
        #
        # return ans[0]

        ans = 1
        for i in range(24):
            matched_bits = 0
            for cand in candidates:
                matched_bits += (1 << i & cand) > 0
            ans = max(ans, matched_bits)
        return ans

        # Lee solution
        #
        # return max(sum(1 << i & a > 0 for a in A) for i in range(24))

        # LC solution
        #
        # return max(sum(n & (1 << i) > 0 for n in candidates) for i in range(0, 24))

        # dic=defaultdict(int)
        # for i in candidates:
        #     index=0
        #     while i!=0:
        #         if i%2!=0:
        #             dic[index]+=1
        #         i=i//2
        #         index+=1
        # ans=0
        # for i in dic:
        #     ans=max(ans,dic[i])
        # return ans


start_time = time()

# _candidates = [16,17,71,62,12,24,14]
# _candidates = [16,16,48,71,62,12,24,14,17,18,19,20,10000]
_candidates = [39,79,15,70,18,8,67,34,71,80,90,22,27,41,95,15,42,70,43,92,77,13,44,71,79,33,46,62,20,81,94,56,79,53,29,71]
# Input: candidates = [16,17,71,62,12,24,14]
# Output: 4
# Explanation: The combination [16,17,62,24] has a bitwise AND of 16 & 17 & 62 & 24 = 16 > 0.
# The size of the combination is 4.
# It can be shown that no combination with a size greater than 4 has a bitwise AND greater than 0.
# Note that more than one combination may have the largest size.
# For example, the combination [62,12,24,14] has a bitwise AND of 62 & 12 & 24 & 14 = 8 > 0.

print(Solution().largestCombination(_candidates))

print("--- %s seconds ---" % (time() - start_time))