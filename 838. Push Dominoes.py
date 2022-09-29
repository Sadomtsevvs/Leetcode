from time import time


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        fall = []
        for i, domino in enumerate(dominoes):
            if domino == 'L' or domino == 'R':
                fall.append((i, domino))
        while fall:
            next_fall = []
            for i, domino in fall:
                if domino == 'L':
                    if i > 0 and dominoes[i-1] == '.':
                        if next_fall and next_fall[-1][0] == i-1 and next_fall[-1][1] == 'R':
                            next_fall.pop()
                        else:
                            next_fall.append((i-1, domino))
                else:
                    if i < len(dominoes) - 1 and dominoes[i+1] == '.':
                        next_fall.append((i+1, domino))
            for i, domino in next_fall:
                dominoes[i] = domino
            fall = next_fall
        return ''.join(dominoes)


start_time = time()

# Example 1:
# Input: dominoes = "RR.L"
# Output: "RR.L"
# Explanation: The first domino expends no additional force on the second domino.
#
_dominoes = ".L.R...LR..L.."
# Example 2:
# Input: dominoes = ".L.R...LR..L.."
# Output: "LL.RR.LLRRLL.."


print(Solution().pushDominoes(_dominoes))

print("--- %s seconds ---" % (time() - start_time))
