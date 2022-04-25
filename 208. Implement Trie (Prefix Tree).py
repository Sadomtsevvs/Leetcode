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

    def search(self, word: str) -> bool:
        cur_node = self.root['']
        for w in word:
            if cur_node[0].get(w) is None:
                return False
            cur_node = cur_node[0][w]
        return cur_node[1]

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.root['']
        for w in prefix:
            if cur_node[0].get(w) is None:
                return False
            cur_node = cur_node[0][w]
        return True


trie = Trie()
trie.insert("hello")
print(trie.search("hell"))
print(trie.search("helloa"))
print(trie.search("hello"))
print(trie.startsWith("hell"))
print(trie.startsWith("helloa"))
print(trie.startsWith("hello"))

