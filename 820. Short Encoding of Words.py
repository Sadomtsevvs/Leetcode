from time import time
from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:

        trie = {}
        cands = []
        for word in set(words):
            node = trie
            for i in range(len(word) - 1, -1, -1):
                char = word[i]
                if char not in node:
                    node[char] = {}
                node = node[char]
            cands.append((node, len(word) + 1))

        return sum(length for node, length in cands if not node)

        # my first solution
        #
        # trie = ({}, 0)
        # for word in set(words):
        #     len_word = len(word)
        #     node = trie[0]
        #     for i in range(len(word) - 1, -1, -1):
        #         char = word[i]
        #         if char not in node:
        #             node[char] = ({}, len_word)
        #         node = node[char][0]
        #
        # ans = [0]
        #
        # def dfs(node):
        #     if not node[0]:
        #         ans[0] += node[1] + 1
        #         return
        #     for key in node[0].keys():
        #         dfs(node[0][key])
        # dfs(trie)
        #
        # return ans[0]

        # official solution
        #
        # words = list(set(words)) #remove duplicates
        # #Trie is a nested dictionary with nodes created
        # # when fetched entries are missing
        # Trie = lambda: collections.defaultdict(Trie)
        # trie = Trie()
        #
        # #reduce(..., S, trie) is trie[S[0]][S[1]][S[2]][...][S[S.length - 1]]
        # nodes = [reduce(dict.__getitem__, word[::-1], trie)
        #          for word in words]
        #
        # #Add word to the answer if it's node has no neighbors
        # return sum(len(word) + 1
        #            for i, word in enumerate(words)
        #            if len(nodes[i]) == 0)

        # Lee solution
        #
        # root = dict()
        # leaves = []
        # for word in set(words):
        #     cur = root
        #     for i in word[::-1]:
        #         cur[i] = cur = cur.get(i, dict())
        #     leaves.append((cur, len(word) + 1))
        # return sum(depth for node, depth in leaves if len(node) == 0)



start_time = time()

_words = ["time", "me", "bell"]
# Input: words = ["time", "me", "bell"]
# Output: 10
# Explanation: A valid encoding would be s = "time#bell#" and indices = [0, 2, 5].
# words[0] = "time", the substring of s starting from indices[0] = 0 to the next '#' is underlined in "time#bell#"
# words[1] = "me", the substring of s starting from indices[1] = 2 to the next '#' is underlined in "time#bell#"
# words[2] = "bell", the substring of s starting from indices[2] = 5 to the next '#' is underlined in "time#bell#"

print(Solution().minimumLengthEncoding(_words))

print("--- %s seconds ---" % (time() - start_time))