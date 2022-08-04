from time import time


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        groups = {}
        for str in strs:
            sort_str = ''.join(sorted(str))
            if sort_str in groups:
                groups[sort_str].append(str)
            else:
                groups[sort_str] = [str]
        return list(groups.values())

        # also nice solution
        #
        # d = {}
        # for w in sorted(strs):
        #     key = tuple(sorted(w))
        #     d[key] = d.get(key, []) + [w]
        # return d.values()

        # solution without sorting
        #
        # result = defaultdict(list)
        # for word in strs:
        #     mask = [0 for _ in range(26)]
        #     for char in word:
        #         mask[ord(char)-ord('a')] += 1
        #     result[tuple(mask)].append(word)
        # return result.values()


start_time = time()

_strs = ["eat","tea","tan","ate","nat","bat"]
_strs = [""]
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

print(Solution().groupAnagrams(_strs))

print("--- %s seconds ---" % (time() - start_time))