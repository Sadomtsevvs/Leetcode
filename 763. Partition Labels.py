from time import time


class Solution:
    def partitionLabels(self, s: str) -> list[int]:

        letters = {}
        for i in range(len(s)):
            if s[i] not in letters:
                letters[s[i]] = [i, i]
            else:
                letters[s[i]][1] = i
        result = []
        last_begin = None
        last_end = None
        for begin, end in letters.values():
            if last_begin is None:
                last_begin = begin
                last_end = end
            elif begin < last_end:
                last_end = max(end, last_end)
            else:
                result.append(last_end - last_begin + 1)
                last_begin = begin
                last_end = end
        result.append(last_end - last_begin + 1)
        return result

        # official solution
        # last = {c: i for i, c in enumerate(s)}
        # j = anchor = 0
        # ans = []
        # for i, c in enumerate(s):
        #     j = max(j, last[c])
        #     if i == j:
        #         ans.append(i - anchor + 1)
        #         anchor = i + 1
        #
        # return ans

        # solution from LC comments
        #
        # rightmost = {c: i for i, c in enumerate(S)}
        # left, right = 0, 0
        # result = []
        # for i, letter in enumerate(S):
        #     right = max(right, rightmost[letter])
        #     if i == right:
        #         result += [right - left + 1]
        #         left = i + 1
        # return result


start_time = time()

_s = "ababcbacadefegdehijhklij"
# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

print(Solution().partitionLabels(_s))

print("--- %s seconds ---" % (time() - start_time))