from time import time


class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:

        if len(coordinates) == 2:
            return True

        x1, y1 = coordinates[0][0], coordinates[0][1]
        x2, y2 = coordinates[1][0], coordinates[1][1]

        special_x = None
        if x2 == x1:
            special_x = x1
        else:
            k = (y2 - y1) / (x2 - x1)
            b = y1 - k * x1

        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            if special_x is not None:
                if x != special_x:
                    return False
            elif y != k*x + b:
                return False
        return True

        # solution from LC comments
        #
        # (x0, y0), (x1, y1) = coordinates[: 2]
        # for x, y in coordinates:
        #     if (x1 - x0) * (y - y1) != (x - x1) * (y1 - y0):
        #         return False
        # return True

        # solution from LC comments
        #
        # (x0, y0), (x1, y1) = coordinates[: 2]
        # return all((x1 - x0) * (y - y1) == (x - x1) * (y1 - y0) for x, y in coordinates)



start_time = time()

_coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
_coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# Output: false

print(Solution().checkStraightLine(_coordinates))

print("--- %s seconds ---" % (time() - start_time))
