from typing import List


class FileSystem:

    def __init__(self):
        self.dirs = {"/": {}}

    def ls(self, path: str) -> List[str]:
        root = self.dirs["/"]
        dirs = path.split("/")
        for dir in dirs:
            if not dir:
                continue
            if (dir, False) in root:
                root = root[(dir, False)]
            elif (dir, True) in root:
                return [dir]
        return sorted([key[0] for key in root.keys()])

    def mkdir(self, path: str) -> None:
        root = self.dirs["/"]
        dirs = path.split("/")
        for dir in dirs:
            if not dir:
                continue
            if (dir, False) not in root:
                root[(dir, False)] = {}
            root = root[(dir, False)]

    def addContentToFile(self, filePath: str, content: str) -> None:
        root = self.dirs["/"]
        dirs = filePath.split("/")
        for dir in dirs:
            if not dir:
                continue
            if (dir, False) in root:
                root = root[(dir, False)]
        if (dir, True) not in root:
            root[(dir, True)] = content
        else:
            root[(dir, True)] += content

    def readContentFromFile(self, filePath: str) -> str:
        root = self.dirs["/"]
        dirs = filePath.split("/")
        for dir in dirs:
            if not dir:
                continue
            if (dir, False) in root:
                root = root[(dir, False)]
        return root[(dir, True)]

        # great Trie solution from comments
        #
        # class TrieNode:
        #
        # def __init__(self):
        #     self.content = ""
        #     self.children = defaultdict(TrieNode)
        #     self.isfile = False
        #
        # class FileSystem:
        #
        # def __init__(self):
        #     self.top = TrieNode()
        #
        # def ls(self, path: str) -> List[str]:
        #     path_lst = path.split("/")
        #     node = self.top
        #     for p in path_lst:
        #         if not p:
        #             continue
        #         node = node.children.get(p)
        #     if node.isfile:
        #         return [p]
        #     ans = [i for i in node.children.keys()]
        #     if not ans:
        #         return ans
        #     ans.sort()
        #     return ans
        #
        # def mkdir(self, path: str) -> None:
        #     path_lst = path.split("/")
        #     node = self.top
        #     for p in path_lst:
        #         if not p:
        #             continue
        #         node = node.children[p]
        #
        # def addContentToFile(self, filePath: str, content: str) -> None:
        #     path_lst = filePath.split("/")
        #     node = self.top
        #     for p in path_lst:
        #         if not p:
        #             continue
        #         node = node.children[p]
        #     node.content += content
        #     node.isfile = True
        #
        # def readContentFromFile(self, filePath: str) -> str:
        #     path_lst = filePath.split("/")
        #     node = self.top
        #     for p in path_lst:
        #         if not p:
        #             continue
        #         node = node.children.get(p)
        #     return node.content


# Your FileSystem object will be instantiated and called as such:
fileSystem = FileSystem()
print(fileSystem.ls("/"))                         # return []
fileSystem.mkdir("/a/b/c")
fileSystem.addContentToFile("/a/b/c/d", "hello")
print(fileSystem.ls("/"))                         # return ["a"]
print(fileSystem.readContentFromFile("/a/b/c/d")) # return "hello"