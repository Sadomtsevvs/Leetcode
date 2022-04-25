class MapSum:

    def __init__(self):
        self.root = {'': [dict(), 0]}

    def insert(self, key: str, val: int) -> None:
        cur_node = self.root['']
        for w in key:
            if cur_node[0].get(w) is None:
                cur_node[0][w] = [dict(), 0]
            cur_node = cur_node[0][w]
        cur_node[1] = val

    def sum(self, prefix: str) -> int:
        cur_node = self.root['']
        for w in prefix:
            if cur_node[0].get(w) is None:
                return 0
            cur_node = cur_node[0][w]

        ans = cur_node[1]
        stack = [cur_node[0]]
        while stack:
            cur_node = stack.pop()
            for node in cur_node.values():
                ans += node[1]
                stack.append(node[0])
        return ans

# official solution
#
# class TrieNode(object):
#     __slots__ = 'children', 'score'
#     def __init__(self):
#         self.children = {}
#         self.score = 0
#
# class MapSum(object):
#     def __init__(self):
#         self.map = {}
#         self.root = TrieNode()
#
#     def insert(self, key, val):
#         delta = val - self.map.get(key, 0)
#         self.map[key] = val
#         cur = self.root
#         cur.score += delta
#         for char in key:
#             cur = cur.children.setdefault(char, TrieNode())
#             cur.score += delta
#
#     def sum(self, prefix):
#         cur = self.root
#         for char in prefix:
#             if char not in cur.children:
#                 return 0
#             cur = cur.children[char]
#         return cur.score


mapSum = MapSum()
mapSum.insert("apple", 3)
print(mapSum.sum("ap"))
mapSum.insert("app", 2)
print(mapSum.sum("ap"))