from time import time
from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # let's make a trie with reversed words
        trie = [{}, None]
        for i in range(len(words)):
            word = words[i]
            node = trie
            for j in range(len(word)-1, -1, -1):
                char = word[j]
                if node[0].get(char) is None:
                    node[0][char] = [{}, None]
                node = node[0][char]
            node[1] = i
        ans = []
        for i in range(len(words)):
            word = words[i]
            node = trie
            check = {}
            for j in range(len(word)):
                char = word[j]
                if node[0].get(char) is None:
                    if node[1] is not None:
                        check[node[1]] = word[j:]
                    break
                node = node[0][char]
                if node[1] is not None:
                    check[node[1]] = word[j+1:]
            else:
                stack = [(node, '')]
                while stack:
                    n_node, pref = stack.pop()
                    if n_node[1] is not None:
                        if n_node[1] != i:
                            check[n_node[1]] = pref
                        elif trie[1] is not None:
                            check[trie[1]] = pref
                    for char, val in n_node[0].items():
                        stack.append((val, pref+char))
            for j, suf in check.items():
                if i != j and suf == suf[::-1]:
                    ans.append([i, j])
        return ans

        # solution from LC comments
        #
        # worddict = dict([(w[::-1], i) for i, w in enumerate(words)])
        # res = []
        # for i, w in enumerate(words):
        #     for j in xrange(len(w) + 1):
        #         prefix, postfix = w[:j], w[j:]
        #         if prefix in worddict and i != worddict[prefix] and postfix == postfix[::-1]:
        #             res.append([i, worddict[prefix]])
        #         if j > 0 and postfix in worddict and i != worddict[postfix] and prefix == prefix[::-1]:
        #             res.append([worddict[postfix], i])
        # return res

        # another from LC
        #
        # d = {}
        # for i, w in enumerate(words):
        #     d[w[::-1]] = i
        # indices = set()
        # for i, w in enumerate(words):
        #     for j in range(len(w) + 1):
        #         prefix = w[:j]
        #         postfix = w[j:]
        #         if prefix in d and i != d[prefix] and postfix == postfix[::-1]:
        #             indices.add((i, d[prefix]))
        #         if postfix in d and i != d[postfix] and prefix == prefix[::-1]:
        #             indices.add((d[postfix], i))
        # return [list(p) for p in indices]


start_time = time()

_words = ["abcd","dcba","lls","s","sssll", ""]
_words = ["bat","tab","cat"]
# _words = ["a",""]
# _words = ["a","aa"]
# _words = ["a","b","c","ab","ac","aa"]
_words = ["a","abc","aba",""]
# Input: words = ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]]
# Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]

print(Solution().palindromePairs(_words))

print("--- %s seconds ---" % (time() - start_time))
