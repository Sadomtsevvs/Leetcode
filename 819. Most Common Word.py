from collections import defaultdict
from time import time
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        words = defaultdict(int)
        cur_word = ''
        symbols = {' ', '!', '?', "'", ',', ';', '.'}
        for char in paragraph:
            if char in symbols:
                if cur_word:
                    cur_word = cur_word.lower()
                    if cur_word not in banned:
                        words[cur_word] += 1
                    cur_word = ''
            else:
                cur_word += char
        cur_word = cur_word.lower()
        if cur_word not in banned:
            words[cur_word] += 1

        most_word = ''
        max_occurs = 0
        for k, v in words.items():
            if v > max_occurs:
                most_word, max_occurs = k, v
        return most_word

        # Lee solution
        #
        # ban = set(banned)
        # words = re.findall(r'\w+', p.lower())
        # return collections.Counter(w for w in words if w not in ban).most_common(1)[0][0]


start_time = time()

_paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
_banned = ["hit"]
# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
# Output: "ball"
# Explanation:
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"),
# and that "hit" isn't the answer even though it occurs more because it is banned.

print(Solution().mostCommonWord(_paragraph, _banned))

print("--- %s seconds ---" % (time() - start_time))
