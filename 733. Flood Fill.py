from time import time


def fill_neighbours(img, i, j, old_color, new_color, size_n, size_m):
    if i < 0 or j < 0 or i == size_n or j == size_m:
        return
    if img[i][j] != old_color:
        return
    img[i][j] = new_color
    fill_neighbours(img, i - 1, j, old_color, new_color, size_n, size_m)
    fill_neighbours(img, i, j - 1, old_color, new_color, size_n, size_m)
    fill_neighbours(img, i, j + 1, old_color, new_color, size_n, size_m)
    fill_neighbours(img, i + 1, j, old_color, new_color, size_n, size_m)

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
        if image[sr][sc] == newColor:
            return image
        fill_neighbours(image, sr, sc, image[sr][sc], newColor, len(image), len(image[0]))
        return image


start_time = time()

_image = [[0, 0, 0], [0, 1, 1]]
_sr = 1
_sc = 1
_newColor = 1

print(Solution().floodFill(_image, _sr, _sc, _newColor))

print("--- %s seconds ---" % (time() - start_time))
