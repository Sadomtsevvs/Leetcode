from time import time


class Solution:
    def matrix(self):
        n = int(input()) * 2 + 1
        mat = [[0 for _ in range(n)] for _ in range(n)]
        black = -1
        for j in range(n):
            for i in range(n):
                if i == j:
                    continue
                if (i + j) % 2 == 0:
                    mat[i][j] = black
                    black -= 1
        white = 1
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if (i + j) % 2 == 1:
                    mat[i][j] = white
                    white += 1
        for row in mat:
            print(*row)


start_time = time()

Solution().matrix()

print("--- %s seconds ---" % (time() - start_time))
