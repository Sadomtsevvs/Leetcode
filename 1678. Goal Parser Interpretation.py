from time import time


class Solution:
    def interpret(self, command: str) -> str:
        return command.replace('()', 'o').replace('(al)', 'al')

        # from LC comments
        #
        # d = {"(al)":"al", "()":"o","G":"G"}
        # tmp= ""
        # res=""
        # for i in range(len(s)):
        #     tmp+=s[i]
        #     if(tmp in d):
        #         res+=d[tmp]
        #         tmp=""
        # return res


start_time = time()

_command = "G()(al)"
# Input: command = "G()(al)"
# Output: "Goal"
# Explanation: The Goal Parser interprets the command as follows:
# G -> G
# () -> o
# (al) -> al
# The final concatenated result is "Goal".

print(Solution().interpret(_command))

print("--- %s seconds ---" % (time() - start_time))
