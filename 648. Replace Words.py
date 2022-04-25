from time import time


class Trie:

    def __init__(self):
        self.root = {'': [dict(), False]}

    def insert(self, word: str) -> None:
        cur_node = self.root['']
        for w in word:
            if cur_node[0].get(w) is None:
                cur_node[0][w] = [dict(), False]
            cur_node = cur_node[0][w]
        cur_node[1] = True

    def get_root(self, word: str) -> str:
        cur_node = self.root['']
        root = ''
        for w in word:
            if cur_node[0].get(w) is None:
                return word
            root += w
            cur_node = cur_node[0][w]
            if cur_node[1]:
                return root
        return word


class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        ans = []
        trie = Trie()
        for d in dictionary:
            trie.insert(d)
        for word in sentence.split():
            ans.append(trie.get_root(word))
        return ' '.join(ans)


start_time = time()

_dictionary = ["cat", "bat", "rat"]
_sentence = "the cattle was rattled by the battery"
# Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"

print(Solution().replaceWords(_dictionary, _sentence))

print("--- %s seconds ---" % (time() - start_time))
