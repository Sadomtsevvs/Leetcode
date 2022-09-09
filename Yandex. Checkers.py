from time import time


class Solution:
    def checkers(self):
        n, m = map(int, input().split(' '))
        set_white = set()
        for _ in range(int(input())):
            set_white.add(tuple(map(int, input().split(' '))))
        set_black = set()
        for _ in range(int(input())):
            set_black.add(tuple(map(int, input().split(' '))))
        color = input()
        if color == 'white':
            first = set_white
            second = set_black
        else:
            first = set_black
            second = set_white
        result = 'No'
        for i, j in first:
            if i + 2 <= n:
                if j + 2 <= m:
                    if (i+1, j+1) in second and (i+2, j+2) not in second and (i+2, j+2) not in first:
                        result = 'Yes'
                        break
                if j - 2 >= 1:
                    if (i+1, j-1) in second and (i+2, j-2) not in second and (i+2, j-2) not in first:
                        result = 'Yes'
                        break
            if i - 2 >= 1:
                if j + 2 <= m:
                    if (i-1, j+1) in second and (i-2, j+2) not in second and (i-2, j+2) not in first:
                        result = 'Yes'
                        break
                if j - 2 >= 1:
                    if (i-1, j-1) in second and (i-2, j-2) not in second and (i-2, j-2) not in first:
                        result = 'Yes'
                        break
        print(result)


start_time = time()

Solution().checkers()

print("--- %s seconds ---" % (time() - start_time))
