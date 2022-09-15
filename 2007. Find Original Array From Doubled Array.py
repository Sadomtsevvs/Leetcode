from collections import defaultdict
from time import time


class Solution:
    def findOriginalArray(self, changed: list[int]) -> list[int]:
        # O(nlogn), not very fast
        # changed.sort()
        # result = []
        # count = dict()
        # for i in range(len(changed)-1, -1, -1):
        #     double = changed[i]*2
        #     if double in count and count[double] > 0:
        #         count[double] -= 1
        #         result.append(changed[i])
        #     else:
        #         count[changed[i]] = count.get(changed[i], 0) + 1
        # if len(result) * 2 == len(changed):
        #     return result
        # return []

        # little optimized solution
        #
        if len(changed) % 2 == 1:
            return []
        changed.sort()
        result = []
        count = defaultdict(int)
        for i in range(len(changed)-1, -1, -1):
            num = changed[i]
            double = num*2
            if double in count and count[double] > 0:
                count[double] -= 1
                result.append(num)
            else:
                count[num] += 1
        if len(result) * 2 == len(changed):
            return result
        return []

        # O(n) solution from LC comments
        #
        # result = []
        #
        # # frequency counter to make sure everything is accounted for
        # cnt = Counter(changed)
        # # track numbers with more than one count not accounted for
        # non_zero_numbers = set(changed)
        #
        # while len(non_zero_numbers) > 0:
        #     # pick a value
        #     value = non_zero_numbers.pop()
        #     non_zero_numbers.add(value)
        #
        #     # find the beginning of the chain
        #     curr = value
        #     while curr // 2 in cnt and cnt[curr // 2] > 0 and curr // 2 != curr and curr % 2 == 0:
        #         curr //= 2
        #
        #     # now build the chain
        #     chain = []
        #     while curr in cnt and cnt[curr] > 0:
        #         chain.append(curr)
        #         if curr * 2 == curr: break
        #         curr *= 2
        #
        #     # handle 0s
        #     if chain[0] == 0:
        #         if cnt[0] % 2 == 0:
        #             result += [0] * (cnt[0] // 2)
        #             cnt[0] = 0
        #             non_zero_numbers.remove(0)
        #         else:
        #             return []
        #         continue
        #
        #     # work through the chain, removing smallest elements first
        #     i = 0
        #     while i < len(chain):
        #         curr_lowest = chain[i]
        #
        #         # none left, skip
        #         if cnt[curr_lowest] == 0:
        #             i += 1
        #             continue
        #
        #         # every number needs something to multiply into
        #         if i + 1 >= len(chain) or cnt[curr_lowest] > cnt[chain[i + 1]]: return []
        #
        #         # do the removal
        #         num_to_remove = min(cnt[curr_lowest], cnt[chain[i + 1]])
        #         cnt[curr_lowest] -= num_to_remove
        #         if cnt[curr_lowest] == 0: non_zero_numbers.remove(chain[i])
        #         cnt[chain[i + 1]] -= num_to_remove
        #         if cnt[chain[i + 1]] == 0: non_zero_numbers.remove(chain[i + 1])
        #
        #         result += [curr_lowest] * num_to_remove
        #
        #         i += 1
        #
        # return result


start_time = time()

_changed = [1, 3, 4, 2, 6, 8]
# _changed = [0,0,0,0]
# _changed = [6,3,0,1]
# Input: changed = [1,3,4,2,6,8]
# Output: [1,3,4]
# Explanation: One possible original array could be [1,3,4]:
# - Twice the value of 1 is 1 * 2 = 2.
# - Twice the value of 3 is 3 * 2 = 6.
# - Twice the value of 4 is 4 * 2 = 8.
# Other original arrays could be [4,3,1] or [3,1,4].

print(Solution().findOriginalArray(_changed))

print("--- %s seconds ---" % (time() - start_time))
