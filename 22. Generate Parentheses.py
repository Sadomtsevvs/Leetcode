from time import time


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        result = []

        def bt(cur, opened, closed):
            if len(cur) == 2*n:
                result.append(cur)
                return
            if opened < n:
                bt(cur + '(', opened + 1, closed)
            if closed < opened:
                bt(cur + ')', opened, closed + 1)

        bt('', 0, 0)

        return result

        # my second solution, 28.03.2023
        #
        # result = []
        #
        # def gen(cur, opened):
        #     if len(cur) == 2 * n:
        #         result.append(cur)
        #     if opened < n:
        #         gen(cur + "(", opened + 1)
        #     if opened > len(cur) // 2:
        #         gen(cur + ")", opened)
        #
        # gen('', 0)
        #
        # return result


start_time = time()

_n = 4
# Output: ["((()))","(()())","(())()","()(())","()()()"]

print(Solution().generateParenthesis(_n))

print("--- %s seconds ---" % (time() - start_time))
