from time import time


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([el[::-1] for el in s.split(' ')])


start_time = time()

data = "Let's take LeetCode contest"
print(Solution().reverseWords(data))

print("--- %s seconds ---" % (time() - start_time))
