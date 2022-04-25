from time import time


class Solution:
    def reverseString(self, s: list[str]) -> None:
        for i in range(len(s)//2):
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]

        # recursive solution
        # middle = len(s)//2
        # def reverse_str(index):
        #     if index < middle:
        #         s[-1 - index], s[index] = s[index], s[-1 - index]
        #         reverse_str(index + 1)
        # reverse_str(0)


start_time = time()

data = ["h","e","l","l","o"]

Solution().reverseString(data)
print(data)

print("--- %s seconds ---" % (time() - start_time))