from time import time


class Solution:
    def removeStars(self, s: str) -> str:

        # my solution
        #
        # result = []
        # for char in reversed(s):
        #     if result and result[-1] == '*' and char != '*':
        #         result.pop()
        #     else:
        #         result.append(char)
        # return ''.join(result)[::-1]

        #  after reading comments
        #
        result = []
        for char in s:
            if char == "*":
                result.pop()
            else:
                result.append(char)
        return ''.join(result)


start_time = time()


# Example 1:
# Input: s = "leet**cod*e"
_s = "leet**cod*e"
# Output: "lecoe"
# Explanation: Performing the removals from left to right:
# - The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
# - The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
# - The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
# There are no more stars, so we return "lecoe".
#
# Example 2:
# Input: s = "erase*****"
# Output: ""
# Explanation: The entire string is removed, so we return an empty string.


print(Solution().removeStars(_s))

print("--- %s seconds ---" % (time() - start_time))
