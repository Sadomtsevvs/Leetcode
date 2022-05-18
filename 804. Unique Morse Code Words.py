from time import time
from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--",
                 "-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        mapping = dict()
        for i in range(len(morse)):
            mapping[chr(i+97)] = morse[i]

        result = set()
        for word in words:
            result.add(''.join(mapping[char] for char in word))

        return len(result)

        # official solution
        #
        # MORSE = [".-","-...","-.-.","-..",".","..-.","--.",
        #          "....","..",".---","-.-",".-..","--","-.",
        #          "---",".--.","--.-",".-.","...","-","..-",
        #          "...-",".--","-..-","-.--","--.."]
        # seen = {"".join(MORSE[ord(c) - ord('a')] for c in word)
        #         for word in words}
        # return len(seen)


start_time = time()

_words = ["gin","zen","gig","msg"]
# Input: words = ["gin","zen","gig","msg"]
# Output: 2
# Explanation: The transformation of each word is:
# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."
# There are 2 different transformations: "--...-." and "--...--.".

print(Solution().uniqueMorseRepresentations(_words))

print("--- %s seconds ---" % (time() - start_time))
