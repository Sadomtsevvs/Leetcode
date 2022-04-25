from time import time


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:

        unique_letters = [set([word[i] for word in words if len(word) > i]) for i in range(10)]

        max_len = max(map(len, words))

        n, m = len(board), len(board[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # creating trie
        trie = {}

        def dfs(node, ii, jj, seen, cur_len):
            if cur_len == max_len:
                return
            for x, y in directions:
                if 0 <= ii + x <= n-1 and 0 <= jj + y <= m-1 and (ii+x, jj+y) not in seen:
                    char = board[ii+x][jj+y]
                    if char not in unique_letters[cur_len]:
                        continue
                    if node.get(char) is None:
                        node[char] = {}
                    next_node = node[char]
                    dfs(next_node, ii+x, jj+y, seen | {(ii+x, jj+y)}, cur_len + 1)

        # filling trie with all possible combinations
        for i in range(n):
            for j in range(m):
                cur = trie
                char = board[i][j]
                if char not in unique_letters[0]:
                    continue
                if cur.get(char) is None:
                    cur[char] = {}
                cur = cur[char]
                dfs(cur, i, j, {(i, j)}, 1)

        ans = []
        for word in words:
            cur = trie
            for char in word:
                if cur.get(char) is None:
                    break
                cur = cur[char]
            else:
                ans.append(word)

        return ans

        # my first solution: I used trie in wrong way: i should put word in trie, not variants
        #
        # first_letters = set(word[0] for word in words)
        # second_letters = set(word[1] for word in words if len(word) > 1)
        #
        # max_len = max(map(len, words))
        #
        # n, m = len(board), len(board[0])
        #
        # directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        #
        # # creating trie
        # trie = {}
        #
        # def dfs(node, ii, jj, seen, cur_len):
        #     if cur_len == max_len:
        #         return
        #     for x, y in directions:
        #         if 0 <= ii + x <= n-1 and 0 <= jj + y <= m-1 and (ii+x, jj+y) not in seen:
        #             char = board[ii+x][jj+y]
        #             if cur_len == 1 and char not in second_letters:
        #                 continue
        #             if node.get(char) is None:
        #                 node[char] = {}
        #             next_node = node[char]
        #             dfs(next_node, ii+x, jj+y, seen | {(ii+x, jj+y)}, cur_len + 1)
        #
        # # filling trie with all possible combinations
        # for i in range(n):
        #     for j in range(m):
        #         cur = trie
        #         char = board[i][j]
        #         if char not in first_letters:
        #             continue
        #         if cur.get(char) is None:
        #             cur[char] = {}
        #         cur = cur[char]
        #         dfs(cur, i, j, {(i, j)}, 1)
        #
        # ans = []
        # for word in words:
        #     cur = trie
        #     for char in word:
        #         if cur.get(char) is None:
        #             break
        #         cur = cur[char]
        #     else:
        #         ans.append(word)
        #
        # return ans

        # best solution from LC comments
        #
        # def dfs(x, y, root):
        #     letter = board[x][y]
        #     cur = root[letter]
        #     word = cur.pop('#', False)
        #     if word:
        #         res.append(word)
        #     board[x][y] = '*'
        #     for dirx, diry in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        #         curx, cury = x + dirx, y + diry
        #         if 0 <= curx < m and 0 <= cury < n and board[curx][cury] in cur:
        #             dfs(curx, cury, cur)
        #     board[x][y] = letter
        #     if not cur:
        #         root.pop(letter)
        #
        # trie = {}
        # for word in words:
        #     cur = trie
        #     for letter in word:
        #         cur = cur.setdefault(letter, {})
        #     cur['#'] = word
        # m, n = len(board), len(board[0])
        # res = []
        # for i in range(m):
        #     for j in range(n):
        #         if board[i][j] in trie:
        #             dfs(i, j, trie)
        # return res


start_time = time()

_board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
_words = ["oath","pea","eat","rain"]
# _board = [["a","b"]]
# _words = ["ab"]
# _board = [["a","a"]]
# _words = ["aaa"]
# _board = [["c","c","c","a","c","b","d","a","d"],["b","e","a","e","e","c","a","c","b"],
#           ["b","c","a","d","a","c","e","d","a"],["c","c","c","a","b","c","a","a","d"],
#           ["d","d","a","d","e","e","e","c","a"],["e","e","b","a","d","a","a","e","c"],
#           ["a","a","d","a","c","c","e","a","d"],["e","d","b","e","b","d","e","e","c"],
#           ["c","a","a","a","c","a","e","b","d"],["a","b","e","b","b","d","e","c","c"],
#           ["a","e","d","e","c","c","e","e","a"]]
# _words = ["addeddeabb"]
# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]

print(Solution().findWords(_board, _words))

print("--- %s seconds ---" % (time() - start_time))
