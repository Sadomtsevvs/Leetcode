from collections import defaultdict
from time import time
from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans = 0
        dic = defaultdict(list)
        for i in range(len(s)):
            dic[s[i]].append(i)
        for word in words:
            numbers = defaultdict(int)
            last_char_taken = defaultdict(int)
            cur_index_s = 0
            for i in range(len(word)):
                char = word[i]
                if char in dic:
                    positions = dic[char]
                    if len(positions) < numbers[char] + 1:
                        break
                    if len(positions) <= last_char_taken[char]:
                        break
                    index = last_char_taken[char]
                    while index < len(positions) and positions[index] < cur_index_s:
                        index += 1
                    if index == len(positions):
                        break
                    cur_index_s = positions[index]
                    last_char_taken[char] = index + 1
                else:
                    break
                numbers[char] += 1
            else:
                ans += 1
        return ans

        # solution from LC, great
        # with using the dictionary of words, which are "waiting" for the first symbol
        #
        # word_dict = defaultdict(list)
        # count = 0
        #
        # for word in words:
        #     word_dict[word[0]].append(word)
        #
        # for char in S:
        #     words_expecting_char = word_dict[char]
        #     word_dict[char] = []
        #     for word in words_expecting_char:
        #         if len(word) == 1:
        #             # Finished subsequence!
        #             count += 1
        #         else:
        #             word_dict[word[1]].append(word[1:])
        #
        # return count


start_time = time()

_s = "abcde"
_words = ["a", "bb", "acd", "ace"]
# Example 1:
# Input: s = "abcde", words = ["a","bb","acd","ace"]
# Output: 3
# Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".

_s = "dsahjpjauf"
_words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
# Example 2:
# Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
# Output: 2

_s = "bbcc"
_words = ["bbcbc"]

_s = "rwpddkvbnnuglnagtvamxkqtwhqgwbqgfbvgkwyuqkdwhzudsxvjubjgloeofnpjqlkdsqvruvabjrikfwronbrdyyjnakstqjac"
_words = ["wpddkvbnn","lnagtva","kvbnnuglnagtvamxkqtwhqgwbqgfbvgkwyuqkdwhzudsxvju","rwpddkvbnnugln",
          "gloeofnpjqlkdsqvruvabjrikfwronbrdyyj","vbgeinupkvgmgxeaaiuiyojmoqkahwvbpwugdainxciedbdkos",
          "mspuhbykmmumtveoighlcgpcapzczomshiblnvhjzqjlfkpina","rgmliajkiknongrofpugfgajedxicdhxinzjakwnifvxwlokip",
          "fhepktaipapyrbylskxddypwmuuxyoivcewzrdwwlrlhqwzikq","qatithxifaaiwyszlkgoljzkkweqkjjzvymedvclfxwcezqebx"]

print(Solution().numMatchingSubseq(_s, _words))

print("--- %s seconds ---" % (time() - start_time))