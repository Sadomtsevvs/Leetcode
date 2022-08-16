from bisect import bisect_left
from time import time
from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        letters = []
        digits = []
        for log in logs:
            words = log.split(' ', 1)
            if words[1][0].isnumeric():
                digits.append(log)
            else:
                letters.append(words)
        letters.sort(key=lambda x: (x[1], x[0]))
        letters = [' '.join(letter) for letter in letters]
        return letters + digits

        # my first solution
        #
        # letters = []
        # digits = []
        # for i in range(len(logs)):
        #     words = logs[i].split(' ')
        #     if words[1].isalpha():
        #         letters.append(logs[i])
        #     else:
        #         digits.append(logs[i])
        # letters.sort(key=lambda x: (x.split(' ', 1)[1], x.split(' ', 1)[0]))
        # return letters + digits

        # first solution, wrong, incorrect to put 1 word into the end
        # letters = []
        # letters_words = []
        # digits = []
        # for i in range(len(logs)):
        #     words = logs[i].split(' ')
        #     if words[1].isalpha():
        #         words = words[1:] + [words[0]]
        #         pos = bisect_left(letters_words, words)
        #         letters_words.insert(pos, words)
        #         letters.insert(pos, logs[i])
        #     else:
        #         digits.append(logs[i])
        # return letters + digits

        # official solution, good example of key function
        #
        # def get_key(log):
        #     _id, rest = log.split(" ", maxsplit=1)
        #     return (0, rest, _id) if rest[0].isalpha() else (1, )
        #
        # return sorted(logs, key=get_key)


start_time = time()

_logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# Example 1:
# Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
# Explanation:
# The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
# The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".

# Example 2:
# Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
# Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

# _logs = ["dig1 8 1 5 1", "let1 art zero can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]

print(Solution().reorderLogFiles(_logs))

print("--- %s seconds ---" % (time() - start_time))
