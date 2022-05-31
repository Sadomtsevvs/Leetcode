from time import time


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:

        to_find = set(range(2**k))
        for i in range(len(s) - k + 1):
            to_find -= {int(s[i:i+k], 2)}
            if not to_find:
                return True
        return False

        # to_find = set()
        # for num in range(2**k):
        #     to_find.add(bin(num)[2:].zfill(k))
        # for i in range(len(s) - k + 1):
        #     to_find -= {s[i:i+k]}
        #     if not to_find:
        #         return True
        # return False

        # official solution 1/1
        #
        # need = 1 << k
        # got = set()
        #
        # for i in range(k, len(s)+1):
        #     tmp = s[i-k:i]
        #     if tmp not in got:
        #         got.add(tmp)
        #         need -= 1
        #         # return True when found all occurrences
        #         if need == 0:
        #             return True
        # return False

        # official solution 1/2
        #
        # got = {s[i - k : i] for i in range(k, len(s) + 1)}
        # return len(got) == 1 << k

        # official solution 2
        #
        # need = 1 << k
        # got = [False]*need
        # all_one = need - 1
        # hash_val = 0
        #
        # for i in range(len(s)):
        #     # calculate hash for s[i-k+1:i+1]
        #     hash_val = ((hash_val << 1) & all_one) | (int(s[i]))
        #     # hash only available when i-k+1 > 0
        #     if i >= k-1 and got[hash_val] is False:
        #         got[hash_val] = True
        #         need -= 1
        #         if need == 0:
        #             return True
        # return False

        # from LC
        #
        # last = int(s[:k], 2)
        # ss = {last}
        # for i in range(k, len(s)):
        #     last = last * 2 - (int(s[i - k]) << k) + int(s[i])
        #     ss.add(last)
        # return len(ss) == 1 << k


start_time = time()

_s = "00110110"
_k = 2
# _s = "0110"
# _k = 2
# Input: s = "00110110", k = 2
# Output: true
# Explanation: The binary codes of length 2 are "00", "01", "10" and "11".
# They can be all found as substrings at indices 0, 1, 3 and 2 respectively.

print(Solution().hasAllCodes(_s, _k))

print("--- %s seconds ---" % (time() - start_time))
