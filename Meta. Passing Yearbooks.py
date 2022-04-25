from time import time


class Solution:
    def findSignatureCounts(self, arr):

        result = [0] * len(arr)
        marked = set()

        def mark_neighbours(i):
            marked.add(i)
            neighbours = [i]
            new_group = {i}
            while neighbours:
                neighbour = neighbours.pop()
                next_neighbour = arr[neighbour-1]
                if next_neighbour in marked:
                    break
                marked.add(next_neighbour)
                new_group.add(next_neighbour)

            for neighbour in new_group:
                result[neighbour - 1] = len(new_group)

        for i in range(1, len(arr) + 1):
            if i in marked:
                continue
            mark_neighbours(i)

        return result


start_time = time()

_arr = [2, 1]
_arr = [1, 3, 2]
# n = 2
# arr = [2, 1]
# output = [2, 2]

print(Solution().findSignatureCounts(_arr))

print("--- %s seconds ---" % (time() - start_time))
