from time import time
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        wordList -= {beginWord}
        ans = 1
        letters = 'abcdefjghigklmonpqrstuvwxyz'
        words = {beginWord}
        while words:
            next_words = set()
            for word in words:
                for i in range(len(word)):
                    for letter in letters:
                        new_word = word[:i] + letter + word[i+1:]
                        if new_word in wordList:
                            if new_word == endWord:
                                return ans + 1
                            next_words.add(new_word)
                            wordList.remove(new_word)
            ans += 1
            words = next_words
        return 0  


start_time = time()

_beginWord = "hit"
_endWord = "cog"
_wordList = ["hot","dot","dog","lot","log","cog"]
# Example 1:
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

_beginWord = "hit"
_endWord = "cog"
_wordList = ["hot","dot","dog","lot","log"]
# Example 2:
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

_beginWord = "ymain"
_endWord = "oecij"
_wordList = ["ymann","yycrj","oecij","ymcnj","yzcrj","yycij","xecij","yecij","ymanj","yzcnj","ymain"]

print(Solution().ladderLength(_beginWord, _endWord, _wordList))

print("--- %s seconds ---" % (time() - start_time))
