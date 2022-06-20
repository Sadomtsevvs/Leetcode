from typing import List


class WordFilter:

    def __init__(self, words: List[str]):

        # let's group repeated words
        grouped_words = {}
        for n, word in enumerate(words):
            grouped_words[word] = n
        filled = set(grouped_words.values())

        pref_trie, suff_trie = {}, {}

        for i in range(len(words)):
            if i not in filled:
                continue
            node = pref_trie
            for w in words[i]:
                if w not in node:
                    node[w] = {}, [i]
                else:
                    node[w][1].append(i)
                node = node[w][0]
            node = suff_trie
            for w in words[i][::-1]:
                if w not in node:
                    node[w] = {}, [i]
                else:
                    node[w][1].append(i)
                node = node[w][0]

        self.pref_trie, self.suff_trie = pref_trie, suff_trie

    def f(self, prefix: str, suffix: str) -> int:
        node = self.pref_trie
        for w in prefix:
            if w not in node:
                return -1
            node, pref_inds = node[w]
        node = self.suff_trie
        for w in suffix[::-1]:
            if w not in node:
                return -1
            node, suff_inds = node[w]
        p_ind = len(pref_inds) - 1
        s_ind = len(suff_inds) - 1
        while p_ind >= 0 and s_ind >= 0:
            if pref_inds[p_ind] == suff_inds[s_ind]:
                return pref_inds[p_ind]
            if pref_inds[p_ind] > suff_inds[s_ind]:
                p_ind -= 1
            else:
                s_ind -= 1
        return -1

# official solution 1
#
# Trie = lambda: collections.defaultdict(Trie)
# WEIGHT = False
#
# class WordFilter(object):
#     def __init__(self, words):
#         self.trie1 = Trie() #prefix
#         self.trie2 = Trie() #suffix
#         for weight, word in enumerate(words):
#             cur = self.trie1
#             self.addw(cur, weight)
#             for letter in word:
#                 cur = cur[letter]
#                 self.addw(cur, weight)
#
#             cur = self.trie2
#             self.addw(cur, weight)
#             for letter in word[::-1]:
#                 cur = cur[letter]
#                 self.addw(cur, weight)
#
#     def addw(self, node, w):
#         if WEIGHT not in node:
#             node[WEIGHT] = {w}
#         else:
#             node[WEIGHT].add(w)
#
#     def f(self, prefix, suffix):
#         cur1 = self.trie1
#         for letter in prefix:
#             if letter not in cur1: return -1
#             cur1 = cur1[letter]
#
#         cur2 = self.trie2
#         for letter in suffix[::-1]:
#             if letter not in cur2: return -1
#             cur2 = cur2[letter]
#
#         return max(cur1[WEIGHT] & cur2[WEIGHT])

# official solution 3
#
# Trie = lambda: collections.defaultdict(Trie)
# WEIGHT = False
#
# class WordFilter(object):
#     def __init__(self, words):
#         self.trie = Trie()
#
#         for weight, word in enumerate(words):
#             word += '#'
#             for i in xrange(len(word)):
#                 cur = self.trie
#                 cur[WEIGHT] = weight
#                 for j in xrange(i, 2 * len(word) - 1):
#                     cur = cur[word[j % len(word)]]
#                     cur[WEIGHT] = weight
#
#     def f(self, prefix, suffix):
#         cur = self.trie
#         for letter in suffix + '#' + prefix:
#             if letter not in cur:
#                 return -1
#             cur = cur[letter]
#         return cur[WEIGHT]


# _words = ['apple', 'app', 'application', 'approve']
_words = ["cabaabaaaa","ccbcababac","bacaabccba","bcbbcbacaa","abcaccbcaa","accabaccaa","cabcbbbcca","ababccabcb","caccbbcbab","bccbacbcba"]
# Your WordFilter object will be instantiated and called as such:
obj = WordFilter(_words)

# _prefix = 'ap'
# _suffix = 'e'
_prefix = 'ab'
_suffix = 'abcaccbcaa'
print(obj.f(_prefix, _suffix))
