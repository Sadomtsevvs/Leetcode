from time import time


class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:

        for w1, w2 in zip(words, words[1:]):
            print(w1, w2)


        abs = {order[i]: i for i in range(len(order))}
        dontskip = set(range(len(words)))
        i = 0
        while dontskip:
        # for i in range(max([len(word) for word in words])):
            newdontskip = set()
            for w in range(len(words) - 1):
                if w not in dontskip:
                    continue
                if len(words[w]) > i and len(words[w+1]) > i:
                    if abs[words[w][i]] > abs[words[w+1][i]]:
                        return False
                    elif abs[words[w][i]] == abs[words[w+1][i]]:
                        newdontskip.add(w)
                        newdontskip.add(w+1)
                elif len(words[w]) > len(words[w+1]):
                    return False
            dontskip = newdontskip
            i += 1
        return True

        # official solution, great
        #
        # order_map = {}
        # for index, val in enumerate(order):
        #     order_map[val] = index
        #
        # for i in range(len(words) - 1):
        #
        #     for j in range(len(words[i])):
        #         # If we do not find a mismatch letter between words[i] and words[i + 1],
        #         # we need to examine the case when words are like ("apple", "app").
        #         if j >= len(words[i + 1]): return False
        #
        #         if words[i][j] != words[i + 1][j]:
        #             if order_map[words[i][j]] > order_map[words[i + 1][j]]: return False
        #             # if we find the first different character and they are sorted,
        #             # then there's no need to check remaining letters
        #             break
        #
        # return True

        # from LC comments
        #
        # order = {key: idx for idx, key in enumerate(order)}
        # order['_'] = -1
        #
        # for w1, w2 in zip(words, words[1:]):
        #     for c1, c2 in zip_longest(w1, w2, fillvalue='_'):
        #         cmp = order[c1] - order[c2]
        #         if cmp > 0: return False
        #         if cmp < 0: break
        #
        # return True


start_time = time()

_words = ["hello", "leetcode"]
_order = "hlabcdefgijkmnopqrstuvwxyz"
_words = ["word","world","row"]
_order = "worldabcefghijkmnpqstuvxyz"
# _words = ["apple","app"]
# _order = "abcdefghijklmnopqrstuvwxyz"
# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

print(Solution().isAlienSorted(_words, _order))

print("--- %s seconds ---" % (time() - start_time))
