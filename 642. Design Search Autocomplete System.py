from typing import List


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        sentences_times = []
        for i in range(len(sentences)):
            sentences_times.append((times[i], sentences[i]))
        sentences_times.sort(key=lambda x: (-x[0], x[1]))
        trie = {}
        for time, sentence in sentences_times:
            node = trie
            for char in sentence:
                if char not in node:
                    node[char] = ({}, [[time, sentence]])
                else:
                    node[char][1].append([time, sentence])
                node = node[char][0]
        self.trie = trie
        self.typed_word = ""

    def input(self, c: str) -> List[str]:
        if c == '#':
            node = self.trie
            for char in self.typed_word:
                if char not in node:
                    node[char] = ({}, [[1, self.typed_word]])
                else:
                    for i, num_word in enumerate(node[char][1]):
                        if num_word[1] == self.typed_word:
                            node[char][1][i][0] += 1
                            break
                    else:
                        node[char][1].append([1, self.typed_word])
                node[char][1].sort(key=lambda x: (-x[0], x[1]))
                node = node[char][0]
            self.typed_word = ""
            return []
        else:
            self.typed_word += c
            node = self.trie
            for char in self.typed_word:
                if char not in node:
                    return []
                words = node[char][1]
                node = node[char][0]
            result = []
            for i in range(min(3, len(words))):
                result.append(words[i][1])
            return result


obj = AutocompleteSystem(["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2])
print(obj.input("i")) # return ["i love you", "island", "i love leetcode"]. There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.
print(obj.input(" ")) # return ["i love you", "i love leetcode"]. There are only two sentences that have prefix "i ".
print(obj.input("a")) # return []. There are no sentences that have prefix "i a".
print(obj.input("#")) # return []. The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search.
print(obj.input("i")) # return ["i love you", "island", "i love leetcode"]. There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.
print(obj.input(" ")) # return ["i love you", "i love leetcode"]. There are only two sentences that have prefix "i ".
print(obj.input("a")) # return []. There are no sentences that have prefix "i a".
print(obj.input("#")) # return []. The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search.
print(obj.input("i")) # return ["i love you", "island", "i love leetcode"]. There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.
print(obj.input(" ")) # return ["i love you", "i love leetcode"]. There are only two sentences that have prefix "i ".
print(obj.input("a")) # return []. There are no sentences that have prefix "i a".
print(obj.input("#")) # return []. The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search.


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)