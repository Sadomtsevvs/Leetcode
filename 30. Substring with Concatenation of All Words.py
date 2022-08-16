from collections import Counter, defaultdict
from time import time
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        len_words = len(words)
        w = len(words[0])
        words = Counter(words)

        ans = []

        def dfs(i, remain, first):
            if not remain:
                ans.append(first)
                return
            if i > n - w:
                return
            word = s[i:i + w]
            if word in words and words[word] > 0:
                words[word] -= 1
                dfs(i + w, remain - 1, first)
                words[word] += 1
            return

        for i in range(len(s) - w * len_words + 1):
            dfs(i, len_words, i)
        return ans

        # official solution, two pointers, sliding window
        #
        # n = len(s)
        # k = len(words)
        # word_length = len(words[0])
        # substring_size = word_length * k
        # word_count = Counter(words)
        #
        # def sliding_window(left):
        #     words_found = defaultdict(int)
        #     words_used = 0
        #     excess_word = False
        #
        #     # Do the same iteration pattern as the previous approach - iterate
        #     # word_length at a time, and at each iteration we focus on one word
        #     for right in range(left, n, word_length):
        #         if right + word_length > n:
        #             break
        #
        #         sub = s[right: right + word_length]
        #         if sub not in word_count:
        #             # Mismatched word - reset the window
        #             words_found = defaultdict(int)
        #             words_used = 0
        #             excess_word = False
        #             left = right + word_length  # Retry at the next index
        #         else:
        #             # If we reached max window size or have an excess word
        #             while right - left == substring_size or excess_word:
        #                 # Move the left bound over continously
        #                 leftmost_word = s[left: left + word_length]
        #                 left += word_length
        #                 words_found[leftmost_word] -= 1
        #
        #                 if words_found[leftmost_word] == word_count[leftmost_word]:
        #                     # This word was the excess word
        #                     excess_word = False
        #                 else:
        #                     # Otherwise we actually needed it
        #                     words_used -= 1
        #
        #             # Keep track of how many times this word occurs in the window
        #             words_found[sub] += 1
        #             if words_found[sub] <= word_count[sub]:
        #                 words_used += 1
        #             else:
        #                 # Found too many instances already
        #                 excess_word = True
        #
        #             if words_used == k and not excess_word:
        #                 # Found a valid substring
        #                 answer.append(left)
        #
        # answer = []
        # for i in range(word_length):
        #     sliding_window(i)
        #
        # return answer


start_time = time()

_s = "barfoothefoobarman"
_words = ["foo","bar"]
# Example 1:
# Input: s = "barfoothefoobarman", words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
# The output order does not matter, returning [9,0] is fine too.

# _s = "wordgoodgoodgoodbestword"
# _words = ["word","good","best","word"]
# Example 2:
# Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
# Output: []
#
_s = "barfoofoobarthefoobarman"
_words = ["bar","foo","the"]
# Example 3:
# Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
# Output: [6,9,12]

print(Solution().findSubstring(_s, _words))

print("--- %s seconds ---" % (time() - start_time))
