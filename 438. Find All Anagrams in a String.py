from time import time


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        result = []
        if len(p) > len(s):
            return result
        dict_p = {}
        for symb in p:
            dict_p[symb] = dict_p.get(symb, 0) + 1
        copy_dict = dict_p.copy()
        first = None
        for i in range(len(s)):
            remain = copy_dict.get(s[i])
            if remain == 0:
                for j in range(first, i):
                    copy_dict[s[j]] += 1
                    first += 1
                    if s[i] == s[j]:
                        break
            if remain is None:
                if first is not None:
                    copy_dict = dict_p.copy()
                    first = None
                continue
            if first is None:
                first = i
            copy_dict[s[i]] -= 1
            if not any(copy_dict.values()):
                result.append(first)
                copy_dict[s[first]] += 1
                first += 1
        return result

        """ solution from comments
        np = len(p)
        ns = len(s)
        if ns < np:
            return []
        pcount = {} # hash map for (char, count) in p
        scount = {} # hash map for (char, count) in s
        output = [] # to store the output indices
        for char in p:
            if char not in pcount:
                pcount[char] = 1
            else:
                pcount[char] += 1
        for i in range(ns):
            char = s[i]
            if char not in scount:
                scount[char] = 1
            else:
                scount[char] += 1
            if i >= np:
                char = s[i - np]
                if scount[char] == 1:
                    del scount[char]
                else:
                    scount[char] -= 1
             if scount == pcount:
                output.append(i - np + 1)
        return output
        """

start_time = time()

_s = "abab"
_p = "ab"

print(Solution().findAnagrams(_s, _p))

print("--- %s seconds ---" % (time() - start_time))