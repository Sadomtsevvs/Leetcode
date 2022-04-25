from time import time
from collections import defaultdict


class Solution:
    def numPairsDivisibleBy60(self, time: list[int]) -> int:

        result = 0
        t_hash = {}
        for t in time:
            k = t_hash.get(t)
            if k:
                t_hash[t] = k + 1
            else:
                t_hash[t] = 1
        while t_hash:
            i, i_num = t_hash.popitem()
            if i_num > 1 and (2 * i) % 60 == 0:
                result += (i_num - 1) * i_num // 2
            for j, j_num in t_hash.items():
                if (i + j) % 60 == 0:
                    result += i_num * j_num
        # return result

        # fast and awesome solution from LC comments
        #
        # time_mod_dict = defaultdict(int)
        # ret = 0
        # for time_i in time:
        #     time_i_mod = time_i % 60
        #     rest_time_mod = (60 - time_i_mod) % 60
        #     if rest_time_mod in time_mod_dict:
        #         ret += time_mod_dict[rest_time_mod]
        #     time_mod_dict[time_i_mod] += 1
        # return ret


start_time = time()

# _time = [60, 30]
_time = [30,20,150,100,40]
# Input: time = [30,20,150,100,40]
# Output: 3
# Explanation: Three pairs have a total duration divisible by 60:
# (time[0] = 30, time[2] = 150): total duration 180
# (time[1] = 20, time[3] = 100): total duration 120
# (time[1] = 20, time[4] = 40): total duration 60

print(Solution().numPairsDivisibleBy60(_time))

print("--- %s seconds ---" % (time() - start_time))
