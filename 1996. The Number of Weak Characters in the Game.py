from time import time
from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # my first solution, MLE
        #
        # properties = [(properties[i][0], properties[i][1], i) for i in range(len(properties))]
        # attacks = sorted(properties, key=lambda x: x[0])
        # defencies = sorted(properties, key=lambda x: x[1])
        # attacks_dict = {}
        # prev = set()
        # bigger = set()
        # prev_property = attacks[-1][0] + 1
        # for i in range(len(properties)-1, -1, -1):
        #     cur = attacks[i][0]
        #     if cur < prev_property:
        #         bigger = prev.copy()
        #         prev_property = cur
        #     attacks_dict[attacks[i][2]] = bigger.copy()
        #     prev.add(attacks[i][2])
        # defencies_dict = {}
        # prev = set()
        # bigger = set()
        # prev_property = defencies[-1][1] + 1
        # for i in range(len(properties)-1, -1, -1):
        #     cur = defencies[i][1]
        #     if cur < prev_property:
        #         bigger = prev.copy()
        #         prev_property = cur
        #     defencies_dict[defencies[i][2]] = bigger.copy()
        #     prev.add(defencies[i][2])
        # result = 0
        # for i in range(len(properties)):
        #     if attacks_dict[i].intersection(defencies_dict[i]):
        #         result += 1
        # return result

        # after readin official
        result = 0
        properties.sort(key=lambda x: (x[0], -x[1]))
        max_def = 0
        for i in range(len(properties)-1, -1, -1):
            cur_def = properties[i][1]
            if cur_def < max_def:
                result += 1
            else:
                max_def = cur_def
        return result




start_time = time()

_properties = [[5,5],[6,3],[3,6]]
# Example 1:
# Input: properties = [[5,5],[6,3],[3,6]]
# Output: 0
# Explanation: No character has strictly greater attack and defense than the other.
#
# Example 2:
# Input: properties = [[2,2],[3,3]]
# Output: 1
# Explanation: The first character is weak because the second character has a strictly greater attack and defense.
#
_properties = [[1,5],[10,4],[4,3]]
# Example 3:
# Input: properties = [[1,5],[10,4],[4,3]]
# Output: 1
# Explanation: The third character is weak because the second character has a strictly greater attack and defense.
# _properties = [[1,1],[2,1],[2,2],[1,2]]

print(Solution().numberOfWeakCharacters(_properties))

print("--- %s seconds ---" % (time() - start_time))