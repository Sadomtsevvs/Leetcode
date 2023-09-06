import math
from time import time
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        ans = []

        cur_len = 0
        cur_words = []
        for word in words:
            if cur_len + len(word) + len(cur_words) > maxWidth:
                line = ""
                spaces = maxWidth - cur_len
                if len(cur_words) == 1:
                    line += cur_words[0]
                    line += " " * spaces
                else:
                    line += cur_words[0]
                    for j in range(1, len(cur_words) - 1):
                        s = math.ceil(spaces / (len(cur_words) - j))
                        spaces -= s
                        line += " " * s
                        line += cur_words[j]
                    line += " " * spaces
                    line += cur_words[-1]
                ans.append(line)
                cur_len = 0
                cur_words = []
            cur_len += len(word)
            cur_words.append(word)
        if cur_words:
            line = ""
            for j in range(len(cur_words)):
                line += cur_words[j]
                if j < len(cur_words) - 1:
                    line += " "
            line += " " * (maxWidth - len(line))
            ans.append(line)

        return ans

        # from comments, amazing and concise
        #
        # res, cur, num_of_letters = [], [], 0
        # for w in words:
        #     if num_of_letters + len(w) + len(cur) > maxWidth:
        #         for i in range(maxWidth - num_of_letters):
        #             cur[i % (len(cur) - 1 or 1)] += ' '
        #         res.append(''.join(cur))
        #         cur, num_of_letters = [], 0
        #     cur += [w]
        #     num_of_letters += len(w)
        # return res + [' '.join(cur).ljust(maxWidth)]


start_time = time()

# Example 1:
# Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
_words = ["This", "is", "an", "example", "of", "text", "justification."]
_maxWidth = 16
# Output:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
#
# Example 2:
# Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
# _words = ["What","must","be","acknowledgment","shall","be"]
# _maxWidth = 16
# Output:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
# Note that the second line is also left-justified because it contains only one word.
#
# Example 3:
# Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
_words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
_maxWidth = 20
# Output:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]

_words = ["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"]
_maxWidth = 16

print(Solution().fullJustify(_words, _maxWidth))

print("--- %s seconds ---" % (time() - start_time))
