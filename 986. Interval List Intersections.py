from time import time


class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        result = []
        first_index = 0
        second_index = 0
        while first_index < len(firstList) and second_index < len(secondList):
            if firstList[first_index][1] < secondList[second_index][0]:
                first_index += 1
            elif secondList[second_index][1] < firstList[first_index][0]:
                second_index += 1
            else:
                result.append([max(firstList[first_index][0], secondList[second_index][0]),
                               min(firstList[first_index][1], secondList[second_index][1])])
                if firstList[first_index][1] < secondList[second_index][1]:
                    first_index += 1
                else:
                    second_index += 1
        return result

start_time = time()

_firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
_secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]

print(Solution().intervalIntersection(_firstList, _secondList))

print("--- %s seconds ---" % (time() - start_time))
