from time import time


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_list = []
        for c in s:
            if c != "#":
                s_list.append(c)
            elif s_list:
                s_list.pop()
        t_list = []
        for c in t:
            if c != "#":
                t_list.append(c)
            elif t_list:
                t_list.pop()
        return "".join(s_list) == "".join(t_list)


start_time = time()

_s = "a##c"
_t = "#a#c"

print(Solution().backspaceCompare(_s, _t))

print("--- %s seconds ---" % (time() - start_time))
