class WordDictionary:

    def __init__(self):
        self.root = {'': [dict(), False]}

    def addWord(self, word: str) -> None:
        cur_node = self.root['']
        for w in word:
            if cur_node[0].get(w) is None:
                cur_node[0][w] = [dict(), False]
            cur_node = cur_node[0][w]
        cur_node[1] = True

    def search(self, word: str) -> bool:
        next_nodes = [self.root['']]
        for w in word:
            if not next_nodes:
                return False
            new_next_nodes = []
            if w == '.':
                for next_node in next_nodes:
                    new_next_nodes += next_node[0].values()
            else:
                for next_node in next_nodes:
                    if next_node[0].get(w) is not None:
                        new_next_nodes.append(next_node[0][w])
            next_nodes = new_next_nodes

        return True if any([n[1] for n in next_nodes]) else False


wordDictionary = WordDictionary()
wordDictionary.addWord("at")
wordDictionary.addWord("and")
wordDictionary.addWord("an")
wordDictionary.addWord("add")
print(wordDictionary.search("a"))
print(wordDictionary.search(".at"))
wordDictionary.addWord("bat")
print(wordDictionary.search(".at"))
print(wordDictionary.search("an."))
print(wordDictionary.search("a.d."))
print(wordDictionary.search("b."))
print(wordDictionary.search("a.d"))
print(wordDictionary.search("."))

# ["WordDictionary","addWord","addWord","addWord","addWord","search","search","addWord","search","search","search","search","search","search"]
# [[],["at"],["and"],["an"],["add"],["a"],[".at"],["bat"],[".at"],["an."],["a.d."],["b."],["a.d"],["."]]